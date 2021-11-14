
from django.urls import path, include
from . import views

app_name = "app"
urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact")
]
