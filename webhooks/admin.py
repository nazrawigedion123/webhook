from django.contrib import admin
from .models import Transaction
# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id' ,
    'amount',
    'currency',
    'created_at_time',
    'timestamp',
    'cause',
    'full_name',
    'account_name',
    'invoice_url',
    'created_at',)




