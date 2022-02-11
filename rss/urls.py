from django.urls import path
from .import views 

urlpatterns = [
    
    path('', views.splash, name='rss-splash'), 
    path('home/', views.home, name='rss-home'),
    path('booking/', views.home, name='rss-booking'), 
     
]