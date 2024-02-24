# Importing required libraries to create customer forms

from .models import Contact, UserProfile
from django import forms


# Defining ContactFrom structure to display in view
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')


# Defining UserProfileForm structure to display in view
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'profile_image', 'describe_yourself')
