import uuid

from django.contrib.auth.models import AbstractUser, Group, PermissionsMixin
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    department_name = models.CharField(max_length=50, unique=True, null=False, verbose_name="Отдел")

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.department_name

    def __repr__(self):
        return f"<Department {self.department_name} id={self.id}>"


class Position(models.Model):
    id = models.BigAutoField(primary_key=True)
    position_name = models.CharField(max_length=30, unique=True, null=False, verbose_name="Должность")

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.position_name

    def __repr__(self):
        return f"<Position {self.position_name} id={self.id}>"


class CustomGroup(Group):
    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роли пользователей"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Group {self.name} id={self.id}>"


class CustomUser(AbstractUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=True, verbose_name="Имя")
    middle_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="Отчество")
    last_name = models.CharField(max_length=30, null=True, verbose_name="Фамилия")
    birthday = models.DateField(null=True, verbose_name="День рождения")
    position = models.ForeignKey(Position, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Должность")
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Отдел")
    phone = PhoneNumberField(blank=True, null=True, verbose_name="Номер телефона")
    role = models.ManyToManyField(CustomGroup, blank=True, verbose_name="Роль")
    is_verification = models.BooleanField(default=False, null=False, verbose_name="Проверен")

    @property
    def full_name(self):
        if self.middle_name is None:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    full_name.fget.short_description = "ФИО"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return f"<User {self.username}: {self.full_name}>"

    def get_all_role_names(self):
        roles = self.role.values_list("name", flat=True)
        roles_set = set(roles)
        return roles_set

    def get_all_categories_for_user(self):
        pass
