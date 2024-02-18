from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Query, Answer

# Register your models here.


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('author', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['id']


@admin.register(Query)
class QueryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'category', 'status', 'author', 'created_on')
    search_fields = ['title', 'category']
    list_filter = ('status', 'author', 'category', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['id', 'category', 'content', 'author', 'created_on']


@admin.register(Answer)
class AnswerAdmin(SummernoteModelAdmin):

    list_display = ('content', 'author', 'created_on')
    search_fields = ['query', 'content', 'author']
    list_filter = ('author', 'created_on')
    readonly_fields = ['id', 'query', 'content', 'author', 'created_on']
