from django.shortcuts import render, redirect
from .models import Account, Operation
from .forms import OperationForm, CategoryForm, AccountForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'expenses/index.html', {'user': request.user})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def manage_operations(request):
    operations_list = Operation.objects.filter(user=request.user)
    return render(request, 'expenses/manage_operations.html', {'operations_list': operations_list})


def new_operation(request):
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            operation = form.save(commit=False)
            operation.user = request.user
            account = Account.objects.get(name=operation.account)
            account.current_balance += operation.type * operation.amount
            account.save()
            operation.save()
            return redirect('index')
    else:
        form = OperationForm()
        return render(request, 'expenses/new_operation.html', {'form': form})


def manage_categories(request):
    categories_list = Account.objects.filter(user=request.user)
    return render(request, 'expenses/manage_categories.html', {'accounts_list': categories_list})


def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.save()
            return redirect('index')
    else:
        form = CategoryForm()
        return render(request, 'expenses/new_category.html', {'form': form})


def manage_accounts(request):
    accounts_list = Account.objects.filter(user=request.user)
    return render(request, 'expenses/manage_accounts.html', {'accounts_list': accounts_list})


def new_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.current_balance = form.cleaned_data.get('initial_balance')
            account.save()
            return redirect('index')
    else:
        form = AccountForm()
        return render(request, 'expenses/new_account.html', {'form': form})

