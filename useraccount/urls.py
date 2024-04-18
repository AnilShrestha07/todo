from django.contrib import admin
from django.urls import path

from useraccount import views

urlpatterns = [
   path('login', views.handle_login,name='login'),
   path('register/', views.handle_register,name='register'),
   path('logout', views.handle_logout,name='logout'),
]