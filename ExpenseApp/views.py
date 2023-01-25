from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

from ExpenseApp.forms import IncomeForm, UserForm,ExpenseForm
from .models import Expense, User,Income
from django.db.models import Sum
# Create your views here.

def openLoginForm(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request,"login.html")

def openUserForm(request):
    form=UserForm()
    return render(request,"signup-form.html",{'form':form})

def login(request):
    phone=request.POST['phone']
    password=request.POST['password']
    result=User.objects.filter(phone=phone,password=password)
    if result:
        data=result.values()
        request.session['user_id']=data[0]['id']
        return redirect('/dashboard')
    else:
        return render(request,"login.html",{'error':'Invalid Phone or Password'})

def logout(request):
    del request.session['user_id']
    return redirect('/')

def signUp(request):
    form=UserForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    return render(request,"signup-form.html",{'result':'Sign Up Successful !'})

def openDashboard(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        incomeResult=user.income_set.aggregate(Sum('amount'))
        expenseResult=user.expense_set.aggregate(Sum('amount'))
        totalIncome=0 if incomeResult['amount__sum'] is None else incomeResult['amount__sum']
        totalExpense=0 if expenseResult['amount__sum'] is None else expenseResult['amount__sum'] 
        currentBalance=totalIncome-totalExpense
        return render(request,"dashboard.html",{'user':user,
        'totalIncome':totalIncome,
        'totalExpense':totalExpense,
        'currentBalance':currentBalance})
    else:
        return redirect('/')

def openIncomeForm(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        form=IncomeForm()
        return render(request,"income-form.html",{'user':user,'form':form})
    else:
        return redirect('/')

def openExpenseForm(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        form=ExpenseForm()
        return render(request,"expense-form.html",{'user':user,'form':form})
    else:
        return redirect('/')

def saveIncome(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        form=IncomeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/all-incomes')
    else:
        return redirect('/')

def saveExpense(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        form=ExpenseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/all-expenses')
    else:
        return redirect('/')

def getAllIncomes(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        incomeResult=user.income_set.all()
        return render(request,"all-income.html",{'incomes':incomeResult,'user':user})
    else:
        return redirect('/')

def deleteIncome(request,id):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        income=Income.objects.get(id=id)
        income.delete()
        return redirect('/all-incomes')
    else:
        return redirect('/')

def deleteExpense(request,id):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        exp=Expense.objects.get(id=id)
        exp.delete()
        return redirect('/all-expenses')
    else:
        return redirect('/')

def openEditIncomeForm(request,id):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        income=Income.objects.get(id=id)
        return render(request,"edit-income-form.html",{'user':user,'income':income})
    else:
        return redirect('/')

def openEditExpenseForm(request,id):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        expense=Expense.objects.get(id=id)
        return render(request,"edit-expense-form.html",{'user':user,'expense':expense})
    else:
        return redirect('/')

def updateIncome(request,id):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        income=Income.objects.get(id=id)
        income.amount=request.POST['amount']
        income.date=request.POST['txn-date']
        income.time=request.POST['txn-time']
        income.category=request.POST['category']
        income.remark=request.POST['remark']
        income.user=user
        income.save()
        return redirect('/all-incomes')
    else:
        return redirect('/')

def updateExpense(request,id):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        expense=Expense.objects.get(id=id)
        expense.amount=request.POST['amount']
        expense.date=request.POST['txn-date']
        expense.time=request.POST['txn-time']
        expense.category=request.POST['category']
        expense.remark=request.POST['remark']
        expense.user=user
        expense.save()
        return redirect('/all-expenses')
    else:
        return redirect('/')


def getAllExpenses(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        expenseResult=user.expense_set.all()
        return render(request,"all-expense.html",{'expenses':expenseResult,'user':user})
    else:
        return redirect('/')

def getIncomeAnalysis(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        result=list(user.income_set.values('category')
        .order_by('category')
        .annotate(total=Sum('amount')))
        return JsonResponse(result,safe=False)
    else:
        return redirect('/')

def getExpenseAnalysis(request):
    if 'user_id' in request.session:
        userid=request.session['user_id']
        user=User.objects.get(id=userid)
        result=list(user.expense_set.values('category')
        .order_by('category')
        .annotate(total=Sum('amount')))
        return JsonResponse(result,safe=False)
    else:
        return redirect('/')