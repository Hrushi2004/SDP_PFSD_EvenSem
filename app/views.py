from django.shortcuts import render


# Create your views here.
def hero(request):
    return render(request, 'Hero.html')


def home(request):
    return render(request, 'Home.html')


