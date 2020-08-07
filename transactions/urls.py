from django.urls import re_path, path
from .views import TransactionViewSets

urlpatterns = [
    path('transactions', TransactionViewSets.as_view({'get': 'list'})),
    path('transaction/<str:pk>',
         TransactionViewSets.as_view({'get': 'retrieve'}))
]
