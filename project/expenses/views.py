from django.shortcuts import render, redirect, get_object_or_404
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    incomes = Income.objects.filter(user = request.user)
    expenses = Expense.objects.filter(user = request.user)
    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    net_income = total_income - total_expense
    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_income': net_income
    }

    return render(request, 'expenses/dashboard.html', context)

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit = False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'expenses/add_income.html', {'form': form})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit = False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

@login_required
def delete_income(request, income_id):
    income = get_object_or_404(Income, id = income_id, user = request.user)
    income.delete()
    return redirect('dashboard')

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Income, id = expense_id, user = request.user)
    expense.delete()
    return redirect('dashboard')
