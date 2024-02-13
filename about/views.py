from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

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
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/contact.html",
        {
            "collaborate_form": collaborate_form
        },
    )