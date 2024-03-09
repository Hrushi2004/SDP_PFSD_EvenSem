from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app.forms import UserForm


# Create your views here.
def hero(request):
    return render(request, 'Hero.html')


def home(request):
    return render(request, 'Home.html')


