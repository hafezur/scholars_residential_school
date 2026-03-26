from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home_function,name="home_function"),
    path('about/', views.about_function,name="about_function"),
    path('feature/', views.feature_function,name="feature_function"),
    path('gallery/', views.galary_function,name="galary_function"),
    path('contact/', views.contact,name="contact_function"),
    path('news&event/', views.newsEvent,name="news&event"),
]
