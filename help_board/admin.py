from django.contrib import admin
from .models import Query, Answer, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('author', 'created_on')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Query)
class QueryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Answer)
class AnswerAdmin(SummernoteModelAdmin):

    list_display = ('query_answer', 'author', 'created_on')
    search_fields = ['query_answer', 'author']
    list_filter = ('author', 'created_on')
    summernote_fields = ('query_answer',)
