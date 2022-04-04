from django.urls import path

from . import views

app_name = 'kladr'

urlpatterns = [
    path('', views.kladr, name='index')
]
