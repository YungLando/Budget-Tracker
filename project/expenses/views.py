from django.shortcuts import render, redirect, get_object_or_404
from .models import Income, Expense, MonthlyIncome, MonthlyExpense
from .forms import IncomeForm, ExpenseForm, MonthlyIncomeForm, MonthlyExpenseForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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

@login_required
def api_delete_income(request, income_id):
    try:
        income = Income.objects.get(id=income_id, user=request.user)
        income.delete()
        return JsonResponse({'status': 'success'})
    except Income.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Income not found'})

@login_required
def api_delete_expense(request, expense_id):
    try:
        expense = Expense.objects.get(id=expense_id, user=request.user)
        expense.delete()
        return JsonResponse({'status': 'success'})
    except Expense.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Expense not found'})

@login_required
def monthly(request):
    incomes = MonthlyIncome.objects.filter(user=request.user)
    expenses = MonthlyExpense.objects.filter(user=request.user)

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
    
    return render(request, 'expenses/monthly.html', context)

@login_required
def add_monthly_income(request):
    if request.method == 'POST':
        form = MonthlyIncomeForm(request.POST)
        if form.is_valid():
            monthly_income = form.save(commit=False)
            monthly_income.user = request.user
            monthly_income.save()
            return redirect('monthly')
    else:
        form = MonthlyIncomeForm()
    return render(request, 'expenses/add_monthly_income.html', {'form': form})

@login_required
def add_monthly_expense(request):
    if request.method == 'POST':
        form = MonthlyExpenseForm(request.POST)
        if form.is_valid():
            monthly_expense = form.save(commit=False)
            monthly_expense.user = request.user
            monthly_expense.save()
            return redirect('monthly')
    else:
        form = MonthlyExpenseForm()
    return render(request, 'expenses/add_monthly_expense.html', {'form': form})

@login_required
def delete_monthly_income(request, income_id):
    income = get_object_or_404(MonthlyIncome, id=income_id, user=request.user)
    if request.method == 'POST':
        income.delete()
        return redirect('monthly_expenses')
    return render(request, 'expenses/confirm_delete.html', {'object': income})

@login_required
def api_delete_monthly_income(request, income_id):
    try:
        monthly_income = get_object_or_404(MonthlyIncome, id=income_id, user=request.user)
        monthly_income.delete()
        return JsonResponse({'status': 'success'})
    except MonthlyIncome.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Monthly income not found'})

@login_required
def delete_monthly_expense(request, expense_id):
    expense = get_object_or_404(MonthlyExpense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('monthly_expenses')
    return render(request, 'expenses/confirm_delete.html', {'object': expense})

@login_required
def api_delete_monthly_expense(request, expense_id):
    try:
        monthly_expense = get_object_or_404(MonthlyExpense, id=expense_id, user=request.user)
        monthly_expense.delete()
        return JsonResponse({'status': 'success'})
    except MonthlyExpense.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Monthly expense not found'})