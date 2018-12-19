from django.urls import path
from .views import customer, employee

app_name = 'webapp'

urlpatterns = [
    path('', customer, name='customer'),
    path('employee/', employee, name='employee'),
    # path('add/', add_customer, name='add'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]