from articles.models import AccessArticlesRule, Article, Category, CategoryArticle

from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ["title", "is_show", "author", "updated"]
    list_filter = ["author", "is_show", "updated", "created"]
    search_fields = ["title", "text"]
    ordering = ("-updated",)


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["category_name"]
    search_fields = ["category_name"]


class CategoryArticleAdmin(admin.ModelAdmin):
    model = CategoryArticle
    list_display = ["article", "category"]
    list_filter = ["category"]
    search_fields = ["article", "category"]


class AccessArticlesRuleAdmin(admin.ModelAdmin):
    model = AccessArticlesRule
    list_display = ["category", "group"]
    list_filter = ["category", "group"]
    search_fields = ["category", "group"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryArticle, CategoryArticleAdmin)
admin.site.register(AccessArticlesRule, AccessArticlesRuleAdmin)
