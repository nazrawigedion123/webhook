from django.urls import path
from . import views

urlpatterns=[
    path("transaction/", views.transaction_webhook, name="transaction_webhook"),
]