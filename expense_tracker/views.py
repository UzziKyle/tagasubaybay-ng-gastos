from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Expense
from .forms import ExpenseForm

# Create your views here.
def home(request):
    expenses = Expense.objects.all()
    context = {'expenses': expenses}
    return render(request, 'expense_tracker/home.html', context)


def add_expense(request):
    context = {}
    if request.method == 'GET':
        context['form'] = ExpenseForm()
        return render(request, 'expense_tracker/expense_form.html', context)
    
    elif request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense has been added!')
            return redirect('home')
        else:
            context['form'] = form
            messages.error(request, 'Please correct the following errors: ')
            return render(request, 'expense_tracker/expense_form.html',  context)
        
        
def edit_expense(request, id):
    context = {}
    expense = get_object_or_404(Expense, id=id)
    
    if request.method == 'GET':
        context['form'] = ExpenseForm(instance=expense)
        context['id'] = id
        
        return render(request, 'expense_tracker/expense_form.html', context)
    
    elif request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense has been updated successfully!')
            return redirect('home')
        
        else:
            context['form'] = form
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'expense_tracker/expense_form.html', context)
    
    
def delete_expense(request, id):
    context = {}
    expense = get_object_or_404(Expense, pk=id)
    context['expense'] = expense
    
    if request.method == 'GET':        
        return render(request, 'expense_tracker/expense_confirm_delete.html', context)
    
    elif request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense has been deleted successfully.')
        return redirect('home')
    