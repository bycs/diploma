from articles.models import Article, Category

from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ["title", "is_show", "author", "updated"]
    list_filter = ["author", "is_show", "updated", "created"]
    search_fields = ["title", "text"]
    ordering = ("-updated",)
    filter_horizontal = ("category",)


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["category_name"]
    search_fields = ["category_name"]
    filter_horizontal = ("group_user",)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
