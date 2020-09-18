from django.urls import path
from . import views


app_name = 'image_search'

urlpatterns = [
    path('howto/', views.how, name='how'),
]
