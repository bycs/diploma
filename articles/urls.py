from django.urls import path

from . import views

urlpatterns = [
    path("", views.articles_list, name="articles_list"),
    path("add/", views.article_add, name="article_add"),
    path("<article_id>/", views.article_detail, name="article_detail"),
]
