from django.contrib import admin
from django.urls import path

from .import views

app_name =  'home_app'

urlpatterns = [
    path('',views.IndexView.as_view(),name='Homepage'),
    path('mixi/',views.TemplateMixi.as_view(),name='mixi'),
]
