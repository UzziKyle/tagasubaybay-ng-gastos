from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense
from .forms import ExpenseForm


# class ExpenseList(ListView):
#     model = Expense.objects.filter(self.request)
#     context_object_name = 'expenses'
#     template_name='expense_tracker/home.html'

# Create your views here.
@login_required
def home(request):
    context = {}
    expenses = Expense.objects.filter(owner=request.user)
    
    if expenses.exists():
        context['expenses'] = expenses
        total = f"{(expenses.aggregate(Sum('amount'))['amount__sum']):.2f}"
        context['total'] = total
        
    return render(request, 'expense_tracker/home.html', context)


@login_required
def add_expense(request):
    context = {}
    
    if request.method == 'GET':
        context['form'] = ExpenseForm()
        return render(request, 'expense_tracker/expense_form.html', context)
    
    elif request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        
        if form.is_valid():
            expense = form.save(commit=False)
            expense.owner = request.user
            expense.save()
            messages.success(request, 'Expense has been added!')
            return redirect('home')
        
        else:
            context['form'] = form
            messages.error(request, 'Please correct the following errors: ')
            return render(request, 'expense_tracker/expense_form.html',  context)
  
        
@login_required   
def edit_expense(request, expense):
    context = {}
    expense = get_object_or_404(Expense, expense=expense)
    
    if request.method == 'GET':
        context['form'] = ExpenseForm(instance=expense)
        context['id'] = expense
        
        return render(request, 'expense_tracker/expense_form.html', context)
    
    elif request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense has been updated successfully!')
            return redirect('home')
        
        else:
            context['form'] = form
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'expense_tracker/expense_form.html', context)
    
  
@login_required  
def delete_expense(request, expense):
    context = {}
    expense = get_object_or_404(Expense, pk=expense)
    context['expense'] = expense
    
    if request.method == 'GET':        
        return render(request, 'expense_tracker/expense_confirm_delete.html', context)
    
    elif request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense has been deleted successfully.')
        return redirect('home')
    