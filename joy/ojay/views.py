from django.shortcuts import render
from django.views.generic import ListView
from .models import Web_edit

class HomePageView(ListView):
    model = Web_edit
    template_name = "home.html"




# Create your views here.
