# Importing libraries required to publish data on django admin panel

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Query, Answer


# Register Category model
@admin.register(Category)
# Using summernote to customize display about info on category page
class CategoryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('author', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['id']


# Register Query model
@admin.register(Query)
# Using summernote to customize display about info on query page
class QueryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'category', 'status', 'author', 'created_on')
    search_fields = ['title', 'category']
    list_filter = ('status', 'author', 'category', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['id', 'category', 'content', 'author', 'created_on']


# Register Answer model
@admin.register(Answer)
# Using summernote to customize display about info on answer page
class AnswerAdmin(SummernoteModelAdmin):

    list_display = ('content', 'author', 'approved', 'created_on')
    search_fields = ['query', 'content', 'author']
    list_filter = ('author', 'created_on')
    readonly_fields = ['id', 'query', 'content', 'author', 'created_on']
