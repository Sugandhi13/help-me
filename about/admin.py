# Importing required libraries to register the models

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, Contact, UserProfile

# Register About model
@admin.register(About)

# Using summernote to customize display about info on admin page
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title', 'content', 'updated_on')
    search_fields = ['title']
    list_filter = ('updated_on',)
    summernote_fields = ('content',)
    readonly_fields = ['id', 'updated_on']


# Register Contact model
@admin.register(Contact)

# Using summernote to customize display contact info on admin page
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'message', 'read', 'created_on')
    search_fields = ['name', 'email']
    list_filter = ('read', 'created_on', 'name')
    readonly_fields = ['id', 'name', 'email', 'message', 'created_on']


# Register UserProfile model
@admin.register(UserProfile)

# Using summernote to customize display user profile info on admin page
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'username', 'describe_yourself', 'updated_on')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ('username', 'updated_on',)
    readonly_fields = ['id', 'username', 'updated_on']