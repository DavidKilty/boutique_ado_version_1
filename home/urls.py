

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Home page route
    path('profile/', views.profile, name='profile'),  # Profile page route
]
