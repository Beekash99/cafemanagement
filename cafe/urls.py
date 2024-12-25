from django.urls import path, include
from django.contrib import admin
from cafe import views
from cafe.views import contact_us_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home_page, name='home_page'),
  path('contact-us/', contact_us_view, name='Contact_Us')
  ]