from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=12)
    class Meta:
        db_table='user'

class Income(models.Model):
    amount=models.FloatField()
    date=models.DateField()
    time=models.TimeField()
    category=models.CharField(max_length=100)
    remark=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='income'

class Expense(models.Model):
    amount=models.FloatField()
    date=models.DateField()
    time=models.TimeField()
    category=models.CharField(max_length=100)
    remark=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='expense'
