from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_usr, name='login'),
    path('logout/', views.logout_usr, name='logout'),
    path('register/', views.register_usr, name='register'),
]