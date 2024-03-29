from django.shortcuts import render


def usersPage(request):
    return render(request, 'users.html')


def customersPage(request):
    return render(request, "customers.html")
