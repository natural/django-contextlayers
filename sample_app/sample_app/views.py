from django.contrib.sites.models import Site
from django.shortcuts import render




def home(request):
    return render(request, 'home.html')
