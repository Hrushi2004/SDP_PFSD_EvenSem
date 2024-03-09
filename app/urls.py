from django.urls import path
from . import views

urlpatterns = [
    path('', views.hero),
    path('home', views.home)
    ]