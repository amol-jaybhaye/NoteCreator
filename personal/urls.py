from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexview, name="index"),
    path('ngo/', views.ngoview, name="ngo"),
    path('q/', views.aboutview, name="about"),
]
