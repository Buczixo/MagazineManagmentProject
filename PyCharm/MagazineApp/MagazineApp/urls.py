"""MagazineApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('glowna/', views.main, name='home'),
    path('test/', views.testBazyDanych, name='test'),
    path('', views.logowanie, name='logowanie'),
    path('wylogowanie/', views.wylogowanie, name='wylogowanie'),
    path('odbior/', views.odbior, name='odbior'),
    path('wydanie/', views.wydanie, name='wydanie'),
    path('przerzucenie/', views.przerzucenie, name='przerzucenie'),
    path('wyszukanie/', views.wyszukanie, name='wyszukanie'),
    path('utworzenie_magazynu/', views.u_magazynu, name='u_magazynu'),
    path('wydruk_magazynu/', views.w_magazynu, name='w_magazynu'),
    path('baza_dostawcow/', views.b_dostawcow, name='b_dostawcow'),
    path('baza_pracownikow/', views.b_pracownikow, name='b_pracownikow'),
    path('baza_towarow/', views.b_towarow, name='b_towarow'),
    path('rejestracja/', views.rejestracja, name='rejestracja')
]
