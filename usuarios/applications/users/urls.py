
from django.contrib import admin
from django.urls import path

from .import views

app_name =  'users_app'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='registrar'),
    path('login/',views.LoginUser.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('update/',views.UpdatePasswordView.as_view(),name='update'),
    path('verificacion/<pk>/',views.CodeVerificationView.as_view(),name='verificacion'),

]
