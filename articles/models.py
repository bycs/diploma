from django.db import models
from django.urls import reverse

from users.models import CustomUser, Role


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30, unique=True, null=False, db_index=True, verbose_name="Заголовок")
    text = models.TextField(null=False, verbose_name="Текст статьи")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    is_show = models.BooleanField(default=False, null=False, verbose_name="Показывать?")
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Автор")

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
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория статьи"
        verbose_name_plural = "Категории статей"

    def __str__(self):
        return self.id

    def __repr__(self):
        return f"<CategoryArticle {self.category_id} для {self.article_id}"


class AccessArticlesRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория статьи")
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Роль пользователя")

    class Meta:
        verbose_name = "Права доступа к статье"
        verbose_name_plural = "Права доступа к статьям"

    def __str__(self):
        return self.id

    def __repr__(self):
        return f"<AccessArticlesRule {self.category_id} для {self.role_id}"
