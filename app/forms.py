from django import forms
from .models import UserProfile, UserData, Blog


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']


class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['first_name', 'last_name', 'date_of_birth']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['username', 'title', 'content']