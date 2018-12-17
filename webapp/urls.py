from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_customer, name='add'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]