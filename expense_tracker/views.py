from django.shortcuts import render
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def home(request):
    return render(request, 'expense_tracker/home.html')


def add_expense(request):
    if request.method == 'GET':
        context = {'form': ExpenseForm()}
        return render(request, 'expense_tracker/expense_form.html', context)
    