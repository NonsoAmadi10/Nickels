from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import Wallet
from .serializers import WalletSerializer


class getAllWalletsViews(ListAPIView):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, ]

    def get_queryset(self):
        queryset = Wallet.objects.filter(owner=self.request.user)
        return queryset


class SingleWalletViews(RetrieveUpdateDestroyAPIView):
    serializer_class = WalletSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get(self, request, *args, **kwargs):
        """Gets a single wallet"""
        wallet = get_object_or_404(Wallet.objects.filter(
            owner=self.request.user), pk=kwargs['uuid'])

        serializer = self.serializer_class(wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """updates a wallet information
        Keyword arguments:
        argument -- request id
        Return: an updated json body
        """

        wallet = get_object_or_404(Wallet.objects.filter(
            owner=self.request.user), pk=kwargs['uuid'])
        serializer = self.serializer_class(
            wallet, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
