from django.contrib import admin
from django.urls import path,include
from Apiv1 import views

urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
]
