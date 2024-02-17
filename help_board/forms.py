from django import forms
from .models import Query, Answer


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('title', 'category', 'content')


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)
