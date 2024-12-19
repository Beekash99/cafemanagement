from django.urls import path, include
from django.contrib import admin
from cafe import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home_page, name='home_page'),
  path('coffee/', views.coffee_list, name='coffee_list'),
]