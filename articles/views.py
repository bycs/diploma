from articles.forms import ArticleAddForm
from articles.models import Article

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render


def articles_list(request):
    articles = Article.objects.filter(is_show=True).all()
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
    return render(request, "articles/article.html", {"article": article})


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
