from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Query, Answer

# Register your models here.


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):

    list_display = ('id', 'title', 'author', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('author', 'created_on')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Query)
class QueryAdmin(SummernoteModelAdmin):

    list_display = ('id', 'title', 'category', 'status', 'created_on')
    search_fields = ['title', 'category']
    list_filter = ('status', 'category', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Answer)
class AnswerAdmin(SummernoteModelAdmin):

    list_display = ('id', 'content', 'author', 'created_on')
    search_fields = ['content', 'author']
    list_filter = ('author', 'created_on')
    summernote_fields = ('content',)
