from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Awesome Jose, this is your 1st index page '
                        'in python!! of our pools application')