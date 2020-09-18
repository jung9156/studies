from django.urls import path
from .views import ReviewListAPI, ReviewDetailAPI

urlpatterns = [
    path('', ReviewListAPI.as_view()),
    path('<int:pk>/', ReviewDetailAPI.as_view()),
]
