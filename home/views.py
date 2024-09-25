# home/views.py

from django.shortcuts import render

# Home page view
def index(request):
    """
    A view to return the index page
    """
    return render(request, 'home/index.html')

# Profile page view
def profile(request):
    """
    A view to return the user's profile page
    """
    return render(request, 'profile.html')
