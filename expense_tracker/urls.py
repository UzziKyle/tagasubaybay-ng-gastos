from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expense/add/', views.add_expense, name='expense-add'),
    path('expense/edit/<int:id>/', views.edit_expense, name='expense-edit'),
    path('expense/delete/<int:id>/', views.delete_expense, name='expense-delete'),
]