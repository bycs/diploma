from django.contrib.auth.models import Group
from django.db import models
from django.urls import reverse

from users.models import CustomUser


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30, unique=True, null=False, db_index=True, verbose_name="Заголовок")
    text = models.TextField(null=False, verbose_name="Текст статьи")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_show = models.BooleanField(default=False, null=False, verbose_name="Показывать?")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Автор")

    class Meta:
        ordering = ("-updated", "created")
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Article {self.title} id={self.id}"

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.id])


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=15, unique=True, null=False, verbose_name="Имя категории")

    class Meta:
        verbose_name = "Список категорий"
        verbose_name_plural = "Список категорий"

    def __str__(self):
        return self.category_name

    def __repr__(self):
        return f"<Category {self.category_name} id={self.id}"


class CategoryArticle(models.Model):
    id = models.BigAutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория статьи"
        verbose_name_plural = "Категории статей"

    def __str__(self):
        return f"{self.article} - {self.category}"

    def __repr__(self):
        return f"<CategoryArticle {self.category} для {self.article}"


class AccessArticlesRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория статьи")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Роль пользователя")

    class Meta:
        verbose_name = "Правило доступа к статье"
        verbose_name_plural = "Правила доступа к статьям"

    def __str__(self):
        return f"{self.category} - {self.group}"

    def __repr__(self):
        return f"<AccessArticlesRule {self.category} для {self.group}"
