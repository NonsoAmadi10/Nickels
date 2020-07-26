from django.db import models
from django.conf import settings

# Create your models here.


class Transactions(models.Model):
    type = (
        ('fund_wallet', 'F_W'),
        ('send_money', 'S_M'),
        ('fund_card', 'F_C'),
        ('savings', '$')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    transaction_type = models.CharField(max_length=35, choices=type)
    nickel_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='owner', on_delete=models.CASCADE)
    amount = models.FloatField(max_length=255)
    origin = models.CharField(null=False, blank=False, max_length=50)
    receiver = models.CharField(
        max_length=10, null=True, blank=True)
