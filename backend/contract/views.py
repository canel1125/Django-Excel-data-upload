from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Contract
from .serializers import ContractSerializer

from .models import Rates
from .serializers import RatesSerializer
# Create your views here.


class ContractListView(APIView):
    def get(self,request, format=None):
        contract = Contract.objects.all()
        serializer= ContractSerializer(contract, many=True)

        return Response(serializer.data)

class RatesView(APIView):
    def get_object(self,contract_slug):
        return Rates.objects.get(contract = contract_slug)
    
    def get(self,request, contract_slug):
        contract = self.get_object(contract_slug)
        serializer = RatesSerializer(contract)
        return Response(serializer.data)
