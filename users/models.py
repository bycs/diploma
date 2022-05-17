import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=True, verbose_name="Имя")
    middle_name = models.CharField(max_length=30, null=True, verbose_name="Отчество")
    last_name = models.CharField(max_length=30, null=True, verbose_name="Фамилия")
    is_verification = models.BooleanField(default=False, null=False, verbose_name="Подтвержден?")

    @property
    def fullname(self):
        if self.middle_name is None:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.username}: {self.fullname}>"


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(max_length=20, unique=True, null=False, verbose_name="Имя роли пользователя")

    class Meta:
        verbose_name = "Список ролей"
        verbose_name_plural = "Список ролей"

    def __str__(self):
        return self.role_name

    def __repr__(self):
        return f"<Role {self.role_name} id={self.id}"


class RoleUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Роль")

    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роли пользователей"

    def __str__(self):
        return self.id

    def __repr__(self):
        return f"<RoleUser {self.role_id} для {self.user_id}"
