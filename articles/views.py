from articles.forms import ArticleAddForm
from articles.models import Article, Category

from django.contrib.auth import get_user
from django.core.exceptions import PermissionDenied
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from users.decorators import staff_required, user_is_staff
from users.models import CustomGroup


def articles_list(request):
    """Формирует список доступных для текущего пользователя статей."""

    if user_is_staff(request):
        articles = Article.objects.filter(is_show=True)
    else:
        current_user = get_user(request)
        roles_user = CustomGroup.objects.filter(customuser=current_user).distinct()
        categories_for_user = Category.objects.filter(role_user__category__role_user__in=roles_user).distinct()
        articles = Article.objects.filter(is_show=True, category__article__category__in=categories_for_user).distinct()

    paginator = Paginator(articles, 5)
    page = request.GET.get("page")

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, "articles/articles_list.html", {"page": page, "articles": articles})


def article_detail(request, article_id: int):
    article = get_object_or_404(Article, id=article_id, is_show=True)

    if request.user.is_superuser or request.user.is_staff:
        has_access = True
    else:
        current_user = get_user(request)
        roles_user = current_user.get_all_role_names()
        roles_users_for_article = article.get_all_access_roles()
        has_access = roles_users_for_article & roles_user

    if not has_access:
        raise PermissionDenied

    return render(request, "articles/article.html", {"article": article})


@staff_required
def article_add(request):
    if request.method == "POST":
        article_form = ArticleAddForm(request.POST)
        if article_form.is_valid() and request.user.is_authenticated:
            new_article = article_form.save(commit=False)
            new_article.author_id = request.user
            new_article.save()
            return render(request, "articles/add_article_done.html", {"new_article": new_article})
    else:
        article_form = ArticleAddForm()
    return render(request, "articles/add_article.html", {"article_form": article_form})
