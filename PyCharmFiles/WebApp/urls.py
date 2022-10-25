from django.urls import path

from . import views

app_name = 'WebApp'
urlpatterns = [
    path('', views.index, name='index'),
]