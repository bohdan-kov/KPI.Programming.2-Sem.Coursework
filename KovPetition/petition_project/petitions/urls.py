from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.create_petition, name='create_petition'),
    path('petitions/', views.petition_list, name='petition_list'),
    path('petition/<int:pk>/', views.petition_detail, name='petition_detail'),  
    path('petition/<int:pk>/delete/', views.delete_petition, name='delete_petition'),
]
