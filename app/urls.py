from django.urls import path
from . import views
from .views import signup_view, signin_view

urlpatterns = [
    path('', views.hero),
    path('home/', views.home),
    path('signup/', signup_view, name='signup_view'),
    path('signup_check/', signin_view, name='signin_view'),
    path('signin/', views.signin),
    ]