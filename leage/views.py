from django.shortcuts import render

# Create your views here.
from leage.models import Postac


def index(request):
    wszystkie = Postac.objects.all()

    dane = {'kategorie': wszystkie}

    return render(request, 'main.html', dane)
