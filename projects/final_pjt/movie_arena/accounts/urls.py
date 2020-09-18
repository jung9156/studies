from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('userlist/', views.userlist, name='userlist'),
    path('management/<user_name>/', views.management, name='management'),
    path('<username>/', views.profile, name='profile'),
    
    
]
