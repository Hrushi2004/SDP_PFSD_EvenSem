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
    CATEGORY_CHOICES = [

        ('Movies', 'Movies'),
        ('Technology', 'Technology'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Fashion', 'Fashion'),
        ('Lifestyle', 'Lifestyle'),
        ('Medical', 'Medical')
        # Add more categories as needed
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    username = models.CharField(max_length=200, default='')  # Specify a default value
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)


    def __str__(self):
        return self.title


class UserUniqueIdentifier(models.Model):
    username = models.CharField(max_length=100, unique=True, default="default_username")
    unique_identifier = models.CharField(max_length=36, unique=True)  # Assuming UUID as unique identifier

    def __str__(self):
        return self.username
