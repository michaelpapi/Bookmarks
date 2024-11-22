from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

# app_name = 'account'

urlpatterns = [

    # Django default auth urls
    path('', include('django.contrib.auth.urls')),    
    # Dashboard url
    path('', views.dashboard, name='dashboard'),
    # Registeration url
    path('register/', views.register, name='register'),
    # For editing profiles
    path('edit/', views.edit, name='edit'),
    # For displaying user lists
    path('users/', views.user_list, name='user_list'),
    # For following people
    path('users/follow/', views.user_follow, name='user_follow'),
    # For displaying users personal info
    path('users/<username>/', views.user_detail, name='user_detail'),
]

