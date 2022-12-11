from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import FinanceDataReader as fdr
import json


class ListCodes(APIView):

    def get(self, request):
        """
        모든 주식 종목 코드 반환
        """
        query_set = Tcode.objects.raw('SELECT * FROM tCode')
        serializer = StockCodeSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyInfo(APIView):

    def get(self, request, **kwargs):
        """
        회사 정보 반환
        """
        company_code = kwargs.get('code')
        query_set = Tcompanyinfo.objects.raw('SELECT * FROM tCompanyInfo WHERE sCode=%s' % company_code)
        serializer = StockCompanySerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DataYear(APIView):

    def get(self, request, **kwargs):
        """
        연 단위 주가 정보 반환
        """
        company_code = kwargs.get('code')
        year = request.query_params.get('year')
        stock_data = json.loads(fdr.DataReader(company_code, str(year)).to_json())
        return Response(stock_data, status=status.HTTP_200_OK)


class DataMonth(APIView):

    def get(self, request, **kwargs):
        """
        월 단위 주가 정보 반환
        """
        company_code = kwargs.get('code')
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        stock_data = json.loads(fdr.DataReader(company_code, datetime(int(year), int(month), 1).isoformat(), (datetime(int(year), int(month), 1) + relativedelta(months=1) - timedelta(days=1)).isoformat()).to_json())
        return Response(stock_data, status=status.HTTP_200_OK)


class DataDay(APIView):

    def get(self, request, **kwargs):
        """
        일 단위 주가 정보 반환
        """
        company_code = kwargs.get('code')
        year = request.query_params.get('year')
        month = request.query_params.get('month')
        day = request.query_params.get('day')
        stock_data = json.loads(fdr.DataReader(company_code, datetime(int(year), int(month), int(day)).isoformat(), datetime(int(year), int(month), int(day)).isoformat()).to_json())
        return Response(stock_data, status=status.HTTP_200_OK)


class StockHolders(APIView):

    def get(self, request, **kwargs):
        """
        주주 정보 반환
        """
        company_code = kwargs.get('code')
        query_set = Tstockholder.objects.raw('SELECT * FROM tStockHolder WHERE sCode=%s' % company_code)
        serializer = StockHolderSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)