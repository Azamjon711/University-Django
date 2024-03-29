from django.urls import path
from .views import usersPage, customersPage

urlpatterns = [
    path('users/', usersPage),
    path('customers/', customersPage)
]
