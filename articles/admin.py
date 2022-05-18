from articles.models import AccessArticlesRule, Article, Category, CategoryArticle

from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ["title", "is_show", "author_id", "updated"]
    list_filter = ["author_id", "is_show", "updated", "created"]
    search_fields = ["title", "text"]


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["category_name"]
    search_fields = ["category_name"]


class CategoryArticleAdmin(admin.ModelAdmin):
    model = CategoryArticle
    list_display = ["article_id", "category_id"]
    list_filter = ["category_id"]
    search_fields = ["article_id", "category_id"]


class AccessArticlesRuleAdmin(admin.ModelAdmin):
    model = AccessArticlesRule
    list_display = ["category_id", "role_id"]
    list_filter = ["category_id", "role_id"]
    search_fields = ["category_id", "role_id"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryArticle, CategoryArticleAdmin)
admin.site.register(AccessArticlesRule, AccessArticlesRuleAdmin)
