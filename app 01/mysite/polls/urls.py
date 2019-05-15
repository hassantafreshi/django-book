from django.urls import path

from . import views

urlpatterns = [
    path('', views.pollpage, name='pollpage'),
]