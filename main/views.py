from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def dost(request):
    return render(request, 'main/dost.html')