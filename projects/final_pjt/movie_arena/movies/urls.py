from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie_detail/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/<int:star_rate>/like/', views.like, name='like'),
    path('<username>/recommend', views.recommend, name='recommend'),
    path('moviecreation/', views.moviecreate, name='moviecreate'),
]
