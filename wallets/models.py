import uuid
from django.utils.crypto import get_random_string
from django.conf import settings
from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    value = models.FloatField(default=0.00)
    wallet_address = models.CharField(
        unique=True, max_length=10, default=get_random_string(length=10))

    def __str__(self):
        return f"{self.value}"

    @property
    def generate_address(self):
        unique_id = get_random_string(length=10)
        self.wallet_address = unique_id
        self.save()
