from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ExpenseList.as_view(), name='home'),
    path('', views.home, name='home'),
    path('expense/add/', views.add_expense, name='expense-add'),
    path('expense/edit/<int:expense>/', views.edit_expense, name='expense-edit'),
    path('expense/delete/<int:expense>/', views.delete_expense, name='expense-delete'),
]