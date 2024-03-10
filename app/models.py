# Assuming your Django app is named 'blog'

# In your models.py file

from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username

class UserData(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    username = models.CharField(max_length=200, default='')  # Specify a default value



class UserUniqueIdentifier(models.Model):
    username = models.CharField(max_length=100, unique=True, default="default_username")
    unique_identifier = models.CharField(max_length=36, unique=True)  # Assuming UUID as unique identifier

    def __str__(self):
        return self.username


