from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import About, UserProfile
from .forms import ContactForm, UserProfileForm

# Create your views here.


def about_me(request):
    """
    Renders the About page

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


def contact(request):
    """
    Renders the About page

    **Template:**

    :template:`about/contact.html`
    """

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks for contacting us. We will respond within 2 working days.'
            )

    contact_form = ContactForm()

    return render(
        request,
        "about/contact.html",
        {
            "contact_form": contact_form
        },
    )


def add_profile(request):
    """
    Renders the About page

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
                "Nice, your profile added successfully! <a href='../view_profile'>Click here</a> to view your information."
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

def view_profile(request):
    """
    Renders the About page

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

