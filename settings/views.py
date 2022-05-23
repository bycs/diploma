from django.shortcuts import render


def index(request):
    """Главная страница портала"""

    return render(request, "index.html")
