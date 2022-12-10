from .models import *
from rest_framework import serializers


class StockCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tcode
        fields = '__all__'


class StockCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tcompanyinfo
        fields = '__all__'


class StockHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tstockholder
        fields = '__all__'


class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tstockprice
        fields = '__all__'


class UserStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuserstocks
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tusers
        exclude = ['userpw']