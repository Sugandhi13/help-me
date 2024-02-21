# Importing required libraries to create query and answer forms
from django import forms
from .models import Query, Answer


# Defining QueryForm structure to display in view
class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('title', 'category', 'content')


# Defining AnswerForm structure to display in view
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)
