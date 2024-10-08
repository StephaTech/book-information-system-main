"""
URL configuration for bis_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from .views import *
# important is names need to be correct look urls.py/models.py/views.py
urlpatterns = [
    path('', home),
    path('home/', home),
    path('members', members_tab),
    path('books', books_tab),
    path('books', books),
    
    path('save', save_member),
    path('members/add', save_member), # I will find reference at member.html form action="members/add"
    path('members/update', save_member),
    path('members/delete', save_member),
    
    path('save', save_book),
    path('books/add', save_book),
    path('books/update', save_book),
    path('books/delete', save_book),

    
   
]
