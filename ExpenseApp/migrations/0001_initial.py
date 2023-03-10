# Generated by Django 4.0.5 on 2022-08-19 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('category', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExpenseApp.user')),
            ],
            options={
                'db_table': 'income',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('category', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExpenseApp.user')),
            ],
            options={
                'db_table': 'expense',
            },
        ),
    ]
