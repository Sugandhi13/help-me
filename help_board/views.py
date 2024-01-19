from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lets_help(request):
    return HttpResponse("Let's help each other!")
