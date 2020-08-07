from django.shortcuts import render, get_object_or_404
from wallets.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import TransactionsSerializer
from .models import Transactions


# Create your views here.

class TransactionViewSets(ViewSet):
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ]

    def list(self, request):
        queryset = Transactions.objects.filter(nickel_user=self.request.user)
        serializer = TransactionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Transactions.objects.filter(nickel_user=self.request.user)
        user = get_object_or_404(queryset, pk=pk)
        serializer = TransactionsSerializer(user)
        return Response(serializer.data)
