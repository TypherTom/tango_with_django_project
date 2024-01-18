from  django.urls import path
from rango import views

app_name = 'rango'

url_patterns = [
    path('', views.index, name='index'),
]