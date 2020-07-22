from django.urls import re_path
from .views import RegistrationAPIView, LoginAPIView


urlpatterns = [
    re_path(r'^register/?$', RegistrationAPIView.as_view()),
    re_path(r'^login/?$', LoginAPIView.as_view())
]
