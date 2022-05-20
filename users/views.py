from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from users.forms import UserRegistrationForm
from users.models import CustomUser


def dashboard(request):
    return render(request, "users/dashboard.html")


def users_list(request):
    users = CustomUser.objects.filter(is_verification=True).order_by("last_name", "first_name", "middle_name").all()
    paginator = Paginator(users, 10)
    page = request.GET.get("page")

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, "users/users_list.html", {"page": page, "users": users})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "registration/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/register.html", {"user_form": user_form})


def error_403(request):
    return render(request, "403.html")


def error_404(request):
    return render(request, "404.html")
