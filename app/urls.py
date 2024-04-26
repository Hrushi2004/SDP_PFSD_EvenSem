from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import signup_view, signin_view

urlpatterns = [
    path('', views.hero),
    path('home/<str:username>/', views.home, name='home'),
    path('signup/', signup_view, name='signup_view'),
    path('signup_check/', signin_view, name='signin_view'),
    path('signin/', views.signin),
    path('profile/<str:username>/', views.profile),
    path('new/<str:username>/', views.new, name='new'),
    path('delete-post/<int:blog_id>/', views.delete_post, name='delete_post'),
    ]