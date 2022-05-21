from django.db import models
from django.urls import reverse

from users.models import CustomGroup, CustomUser


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=15, unique=True, null=False, verbose_name="Категория")
    role_user = models.ManyToManyField(CustomGroup, verbose_name="Роль пользователя")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category_name

    def __repr__(self):
        return f"<Category {self.category_name} id={self.id}>"


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30, unique=True, null=False, db_index=True, verbose_name="Заголовок")
    text = models.TextField(null=False, verbose_name="Текст статьи")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_show = models.BooleanField(default=False, null=False, verbose_name="Показывать?")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ManyToManyField(Category, verbose_name="Категория")

    class Meta:
        ordering = ("-updated", "created")
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Article {self.title} id={self.id}>"

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.id])

    def get_all_access_roles(self):
        categories = self.category.all()
        roles = set()
        for category in categories:
            roles = roles | set(category.role_user.values_list("name", flat=True))
        return roles
