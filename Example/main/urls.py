from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.too, name='too'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
]
