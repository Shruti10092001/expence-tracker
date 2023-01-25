from django.urls import path
from . import views

urlpatterns = [
    path('',views.openLoginForm),
    path('user-form',views.openUserForm),
    path('save-user',views.signUp),
    path('dashboard',views.openDashboard),
    path('login',views.login),
    path('logout',views.logout),
    path('income-form',views.openIncomeForm),
    path('save-income',views.saveIncome),
    path('expense-form',views.openExpenseForm),
    path('save-expense',views.saveExpense),
    path('all-incomes',views.getAllIncomes),
    path('all-expenses',views.getAllExpenses),
    path('del-income/<int:id>',views.deleteIncome),
    path('del-expense/<int:id>',views.deleteExpense),
    path('edit-income/<int:id>',views.openEditIncomeForm),
    path('edit-expense/<int:id>',views.openEditExpenseForm),
    path('update-expense/<int:id>',views.updateExpense),
    path('update-income/<int:id>',views.updateIncome),
    path('income-analysis',views.getIncomeAnalysis),
    path('expense-analysis',views.getExpenseAnalysis)
]