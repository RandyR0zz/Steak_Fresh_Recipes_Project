"""Steak_Fresh_Recipes_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipes_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.show_homepage, name='home'),
    path('note/', views.show_note, name='show_details'),
    path('', views.show_homepage),
    path('posts/', views.show_all_posts, name='posts'),
    path('posts/<int:id>', views.show_post, name='post'),
    path('about/', views.show_history_page, name='about'),
    path('posts/add/', views.add_post, name='add_post'),
]