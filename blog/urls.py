from django.urls import path

from .import views


urlpatterns = [
    path('',views.index),
    path('index', views.index),
    path('movies', views.movies),
    path('series', views.series),
    path('books', views.books),
]
