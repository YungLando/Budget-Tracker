"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('add_income/', views.add_income, name = 'add_income'),
    path('add_expense/', views.add_expense, name = 'add_expense'),
    path('delete_income/<int:income_id>/', views.delete_income, name = 'delete_income'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name = 'delete_expense'),
    path('api/delete_income/<int:income_id>/', views.api_delete_income, name = 'api_delete_income'),
    path('api/delete_expense/<int:expense_id>/', views.api_delete_expense, name = 'api_delete_expense'),
    path('monthly/', views.monthly, name='monthly'),
    path('add_monthly_income/', views.add_monthly_income, name='add_monthly_income'),
    path('add_monthly_expense/', views.add_monthly_expense, name='add_monthly_expense'),
    path('delete_monthly_income/<int:income_id>/', views.delete_monthly_income, name='delete_monthly_income'),
    path('delete_monthly_expense/<int:expense_id>/', views.delete_monthly_expense, name='delete_monthly_expense'),
    path('api/delete_monthly_income/<int:income_id>/', views.api_delete_monthly_income, name='api_delete_monthly_income'),
    path('api/delete_monthly_expense/<int:expense_id>/', views.api_delete_monthly_expense, name='api_delete_monthly_expense'),
]
