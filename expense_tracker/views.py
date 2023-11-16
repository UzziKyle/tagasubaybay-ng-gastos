from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def home(request):
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'expense_tracker/home.html', context)


def add_expense(request):
    if request.method == 'GET':
        context = {'form': ExpenseForm()}
        return render(request, 'expense_tracker/expense_form.html', context)
    
    elif request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'expense_tracker/expense_form.html',  {'form': form})