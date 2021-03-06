# Generated by Django 4.0.4 on 2022-05-23 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=15, unique=True, verbose_name="Категория")),
                ("role_user", models.ManyToManyField(to="users.customgroup", verbose_name="Роль пользователя")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ("category_name",),
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(db_index=True, max_length=50, unique=True, verbose_name="Заголовок")),
                ("text", models.TextField(verbose_name="Текст статьи")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Дата изменения")),
                ("is_show", models.BooleanField(default=False, verbose_name="Показывать?")),
                (
                    "author",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                ("category", models.ManyToManyField(to="articles.category", verbose_name="Категория")),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
                "ordering": ("-updated", "-created"),
            },
        ),
    ]
