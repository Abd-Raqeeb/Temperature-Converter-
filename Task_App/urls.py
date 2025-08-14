from django.urls import path

from . import views

urlpatterns = [
    path('', views.temp_convertor, name='temp_convertor'),  # Home page   
]
