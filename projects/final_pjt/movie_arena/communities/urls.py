from django.urls import path
from . import views


app_name = 'communities'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/delete/<int:article_pk>/', views.delete, name='delete'),
    path('article/update/<int:article_pk>/', views.update, name='update'),
    path('comment/delete/<int:article_pk>/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
    path('article/<str:article_color>/', views.article_color, name='color'),
    path('article/<str:article_color>/<int:article_pk>/', views.detail, name='detail'),
    path('create/<str:article_color>/', views.create, name='create'),
]