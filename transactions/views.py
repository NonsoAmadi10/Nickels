from django.shortcuts import render
from wallets.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .serializers import TransactionsSerializer
from .models import Transactions


# Create your views here.


class AllTransactionsView(ListAPIView):
    """ Gets all transaction belonging to an authenticated user

    Keyword arguments:
    decrypted_token -- a decrypted jwt oken
    Return: returns a response in JSON format
    """

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ]
    serializer_class = TransactionsSerializer

    def get_queryset(self):
        query_set = Transactions.objects.filter(nickel_user=self.request.user)
        return query_set
