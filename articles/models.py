import uuid

from django.db import models

from users.models import CustomUser, Role


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30, unique=True, null=False, db_index=True)
    text = models.TextField(null=False)
    is_show = models.BooleanField(default=True, null=False)
    # to do column author_id
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __repr__(self):
        return f"<Article {self.title} id={self.id}"


class CategoryArticle(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=30, unique=True, null=False)


# to do class AccessArticlesRule
class AccessArticlesRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
