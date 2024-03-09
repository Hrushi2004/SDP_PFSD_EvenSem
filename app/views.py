from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from app.forms import UserForm


# Create your views here.
def hero(request):
    return render(request, 'Hero.html')


def home(request):
    return render(request, 'Home.html')


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
            messages.error(request, "Password should be at least 8 characters long and contain letters, numbers, and special characters")
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




def signin_view(request):
    if request.method == 'POST':
        in_username = request.POST.get('signin-username')
        in_password = request.POST.get('signin-password')

        # Check if the username and password pair exists in the database
        user_exists = UserProfile.objects.filter(username=in_username, password=in_password).exists()

        if user_exists:
            # Create a session for the user
            user = UserProfile.objects.get(username=in_username)
            request.session['user_id'] = user.id

            # Optionally, you can set other session data if needed
            request.session['username'] = user.username

            # Redirect to a success page or any other page
            return redirect('/home')  # Replace 'home' with your desired URL name
        else:
            # Authentication failed
            error_message = "Invalid username or password"
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        # Handle GET request if needed
        return render(request, 'signin.html')
