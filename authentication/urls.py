from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='loginUser'),
    path('register/', views.registerUser, name='registerUser')
    
]