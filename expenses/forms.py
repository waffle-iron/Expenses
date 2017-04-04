from django.forms import ModelForm
from expenses.models import Operation, Category, Account


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = ['account', 'type', 'category', 'date', 'amount']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color']


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'currency', 'initial_balance']
