from django import forms
from django.core.exceptions import ValidationError

from django.forms import widgets

from webapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("name", "email", "text")
        labels = {
            'name': 'Имя пользователя',
            'email': 'Email',
            'text': 'Текст',
        }

    def clean_text(self):
        text = self.cleaned_data.get("text")
        if len(text) <= 2:
            raise ValidationError("Меньше 2 символов не должно быть!")
        return text

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) <= 2:
            raise ValidationError("Меньше 2 символов не должно быть!")
        return name