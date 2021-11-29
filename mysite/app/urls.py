
from django.urls import path, include
from . import views
from django.contrib import admin
app_name = "app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('donate/', views.donate, name="donate"),
    path('events/', views.event, name="events"),
    path('volunteer/', views.volunteer, name="volunteer")
]
