from django.urls import path
from .views import Stock

urlpatterns = [
    path('', Stock.as_view(), name='main'),
]