from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
#    path('register/', views.registerUser, name='registerUser')
    path('createpost/', views.createpost, name='createpost'),
    
]