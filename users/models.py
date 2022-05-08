from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(max_length=30, unique=True, null=False)


class RoleUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
