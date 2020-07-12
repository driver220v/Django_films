from django.urls import path

from . import views

urlpatterns = [
    path('all', views.all_films, name='scrapper-all'),
    path('one', views.all_films, name='scrapper-one')
]
