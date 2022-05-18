from articles.models import Article

from django import forms


class ArticleAddForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "text")
