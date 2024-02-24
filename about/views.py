# Importing libraries required to build views

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import About, Contact, UserProfile
from .forms import ContactForm, UserProfileForm


# Created about_me view that renders all info of about model
def about_me(request):
    """
    Display an individual :model:`about.About`.

    **Context**

    ``Query``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about.html`
    """

    aboutset = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {
            "about": aboutset
        },
    )


# Created contact view that renders info of contact form & update contact model
def contact(request):
    """
    Display an individual :Form:`about.forms.ContactForm`
    and insert record in Contact model.

    **Context**

    ``Query``
        An instance of :model:`about.Contact`.

    **Template:**

    :template:`about/contact.html`
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks for contacting us. We will respond within 2 days.'
            )

    contact_form = ContactForm()

    return render(
        request,
        "about/contact.html",
        {
            "contact_form": contact_form
        },
    )


# Created add_profile view that renders all info of
# add profile form and update user profile model
def add_profile(request):
    """
    Display an individual :Form:`about.forms.UserProfileForm`
    and insert record in UserProfile model.

    **Context**

    ``Query``
        An instance of :model:`about.UserProfile`.

    **Template:**

    :template:`about/add_profile.html`
    """

    if request.method == "POST":
        user_profile_form = UserProfileForm(data=request.POST)
        if user_profile_form.is_valid():
            profile = user_profile_form.save(commit=False)
            profile.username = request.user
            profile.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Profile added! <a href='../view_profile'>View_Profile</a>"
            )
    else:
        user_profile_form = UserProfileForm()

    return render(
        request,
        "about/add_profile.html",
        {
            "user_profile_form": user_profile_form
        },
    )


# Created view_profile view that renders all info of
# view user profile form from user profile model
def view_profile(request):
    """
    Display an individual :Form:`about.forms.UserProfileForm`
    and displays a record of logged in user from UserProfile model.

    **Context**

    ``Query``
        An instance of :model:`about.UserProfile`.

    **Template:**

    :template:`about/view_profile.html`
    """

    queryset = UserProfile.objects.filter(username=request.user)
    user_profile = get_object_or_404(queryset)

    return render(
        request,
        "about/view_profile.html",
        {
            "user_profile": user_profile
        },
    )
