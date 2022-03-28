from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('gettoken/<str:id>/<str:token>/', views.genrate_token, name="token.generate"),
    path('process/<str:id>/<str:token>/', views.process_payment, name="payment.process"),
]