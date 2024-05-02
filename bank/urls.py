
from django.urls import path

from bank.views import BankAPIView1, BankAPIView2

urlpatterns = [
    path("part1", BankAPIView1.as_view()),
    path("data", BankAPIView2.as_view()),
]
