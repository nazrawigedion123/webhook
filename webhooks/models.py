from django.db import models

# Create your models here.

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at_time = models.BigIntegerField()
    timestamp = models.BigIntegerField()
    cause = models.CharField(max_length=255)
    full_name = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    invoice_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
