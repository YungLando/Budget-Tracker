# Generated by Django 4.0.4 on 2024-06-10 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_monthlyincome_monthlyexpense'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='description',
        ),
        migrations.RemoveField(
            model_name='monthlyexpense',
            name='description',
        ),
    ]
