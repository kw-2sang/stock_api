from django.urls import path
from .views import *

urlpatterns = [
    path('', ListCodes.as_view(), name='main'),
    path('<str:code>', CompanyInfo.as_view(), name='company'),
    path('data/year/<str:code>', DataYear.as_view(), name='year'),
    path('data/month/<str:code>', DataMonth.as_view(), name='month'),
    path('data/day/<str:code>', DataDay.as_view(), name='day'),
    path('holders/<str:code>', StockHolders.as_view(), name='holders'),
]