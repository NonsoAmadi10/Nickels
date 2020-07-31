from django.urls import re_path
from .views import AllTransactionsView

urlpatterns = [
    re_path('^transactions', AllTransactionsView.as_view())
]
