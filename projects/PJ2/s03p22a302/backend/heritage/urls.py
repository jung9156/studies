from django.urls import path
from .views import HeritageListAPI, HeritageDetailAPI

urlpatterns = [
    path('', HeritageListAPI.as_view()),
    path('<int:pk>/', HeritageDetailAPI.as_view()),
]
