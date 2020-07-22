from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    value = serializers.FloatField()

    class Meta:
        model = Wallet
        fields = '__all__'
