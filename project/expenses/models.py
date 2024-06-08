from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#ideas
#taxes
#api for bank account
#api for digital subscriptions
class Income(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    source = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    date = models.DateField()

    def __str__(self):
        return f"{self.source}: {self.amount}"
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.description}: {self.amount}"
