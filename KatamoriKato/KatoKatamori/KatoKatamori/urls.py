from django.contrib import admin
from django.urls import path
from HomePage import views

urlpatterns = [
    path('', views.HomePage),
]
