from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Blog
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from app.forms import UserForm, UserDataForm, BlogForm


# Create your views here.
def hero(request):
    return render(request, 'Hero.html')


def home(request, username):
    try:
        # Assuming the unique identifier is associated with the user's username
        userid = UserUniqueIdentifier.objects.get(username=username)
    except UserUniqueIdentifier.DoesNotExist:
        # Handle case where user is not found
        return HttpResponse("User not found")

    # Now you have the user's unique identifier, you can use it to fetch related blogs or perform other operations
    blogs = Blog.objects.all()  # Assuming 'author' field in Blog model stores the user
    return render(request, 'home.html', {'blogs': blogs, 'username': username})


def signin(request):
    return render(request, 'signin.html')


from django.contrib import messages

import re


def signup_view(request):
    if request.method == 'POST':
        # Get form data from POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Regular expressions for input validation
        username_regex = r'^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$'
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        password_regex = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        # Validate username format
        if not re.match(username_regex, username):
            messages.error(request, "Username should contain a mix of letters and numbers")
            return redirect('/#signup')

        # Validate email format
        if not re.match(email_regex, email):
            messages.error(request, "Invalid email format")
            return redirect('/#signup')

        # Validate password format
        if not re.match(password_regex, password):
            messages.error(request,
                           "Password should be at least 8 characters long and contain letters, numbers, and special characters")
            return redirect('/#signup')

        try:
            # Check if username or email already exists in the database
            existing_user = UserProfile.objects.filter(username=username).exists()
            existing_email = UserProfile.objects.filter(email=email).exists()

            if existing_user:
                messages.error(request, "Username already exists")
                return redirect('/#signup')

            if existing_email:
                messages.error(request, "Email already exists")
                return redirect('/#signup')

            # Create a new User object with the form data
            new_user = UserProfile(username=username, email=email, password=password)

            # Save the user object to the database
            new_user.save()

            # Redirect to a success page or any other page
            messages.success(request, "New account created, login to continue")
            return redirect('/signin')

        except Exception as e:
            messages.error(request, str(e))
            return redirect('/#signup')

    else:
        # Pass any existing messages to the template context
        messages.get_messages(request)

        # Handle GET request if needed
        return render(request, 'signup.html')


from uuid import uuid4
from .models import UserUniqueIdentifier  # Import the model you created

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('signin-username')
        password = request.POST.get('signin-password')

        # Custom authentication logic to authenticate the user
        user = authenticate_user(username, password)

        if user is not None:
            # Generate a unique identifier for the user
            user_unique_identifier = str(uuid4())

            # Store the unique identifier in the user's session
            request.session['user_unique_identifier'] = user_unique_identifier

            # Store the username and unique identifier in the database
            user_identifier_obj, created = UserUniqueIdentifier.objects.get_or_create(
                username=username,
                defaults={'unique_identifier': user_unique_identifier}
            )

            # Redirect to the home page with the unique identifier in the URL
            return redirect(f'/home/{username}')
        else:
            # Authentication failed
            error_message = "Invalid username or password"
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')


def profile(request, username):
    user_blogs = Blog.objects.filter(username=username)
    return render(request, 'Profile.html', {'blogs': user_blogs, 'username': username})


from django.shortcuts import render


def new(request, username):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home', username=username)
    else:
        form = BlogForm()

    # Pass the username to the template context
    context = {'form': form, 'username': username}
    return render(request, 'NewPost.html', context)



def authenticate_user(username, password):
    try:
        # Retrieve the user from the database based on the provided username
        user = UserProfile.objects.get(username=username)

        # Check if the provided password matches the user's password
        if user.password == password:
            return user
        else:
            return None  # Password doesn't match
    except UserProfile.DoesNotExist:
        return None  # User with the provided username doesn't exist

def delete_post(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.delete()
        return JsonResponse({'message': 'Blog post deleted successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)