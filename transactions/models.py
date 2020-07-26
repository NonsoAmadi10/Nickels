from datetime import datetime
from django.db import models
from djang.conf import settings

# Create your models here.


class Transactions(models.Model):
    type = (
        ('fund_wallet', 'F_W'),
        ('send_money', 'S_M'),
        ('fund_card', 'F_C'),
        ('savings', '$')
    )

    date_created = models.DateTimeField(
        auto_now_add=True, default=datetime.utcnow())
    transaction_type = models.CharField(max_length=35, choices=type)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='', on_delete=models.CASCADE)
    amount = models.FloatField(max_length=255)
