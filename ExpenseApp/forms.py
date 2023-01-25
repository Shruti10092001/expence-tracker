from dataclasses import fields
from turtle import width
from .models import User,Income,Expense
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'placeholder':"Enter name",'class':'form-control'}),
            'phone':forms.TextInput(attrs={'placeholder':'Enter Phone','class':'form-control'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Email','class':'form-control'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'form-control'}),
            'profilePic':forms.FileInput(attrs={'class':'form-control'})
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields="__all__"
        widgets={
            'amount':forms.TextInput(attrs={'placeholder':"Enter amount",'class':'form-control'}),
            'date':forms.DateInput(format=('%d-%m-%Y'),attrs={'class':'form-control','type':'date'}),
            'time':forms.TimeInput(format=('%H:%M'),attrs={'class':'form-control','type':'time'}),
            'category':forms.TextInput(attrs={'placeholder':"Enter Category",'class':'form-control'}),
            'remark':forms.TextInput(attrs={'placeholder':"Enter name",'class':'form-control'})
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields="__all__"
        widgets={
            'amount':forms.TextInput(attrs={'placeholder':"Enter amount",'class':'form-control'}),
            'date':forms.DateInput(format=('%d-%m-%Y'),attrs={'class':'form-control','type':'date'}),
            'time':forms.TimeInput(format=('%H:%M'),attrs={'class':'form-control','type':'time'}),
            'category':forms.TextInput(attrs={'placeholder':"Enter Category",'class':'form-control'}),
            'remark':forms.TextInput(attrs={'placeholder':"Enter name",'class':'form-control'})
        }