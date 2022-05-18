import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30, null=True, verbose_name="Имя")
    middle_name = models.CharField(max_length=30, null=True, verbose_name="Отчество")
    birthday = models.DateField(verbose_name="День рождения", null=True)
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
