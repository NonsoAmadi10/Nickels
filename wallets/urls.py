from django.urls import re_path
from .views import SingleWalletViews, getAllWalletsViews


urlpatterns = [
    re_path('^wallets', getAllWalletsViews.as_view()),
    re_path(
        r'^wallet/(?P<uuid>([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}){1})/$', SingleWalletViews.as_view())
]
