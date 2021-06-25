from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *



def index(request):
    wszystkie = Postac.objects.all()

    dane = {'kategorie': wszystkie}

    return render(request, 'main.html', dane)


