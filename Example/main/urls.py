from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    #path('nav', views.nav),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
]
