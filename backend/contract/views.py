from datetime import date
from os import name
from django.http import Http404
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.defaultfilters import slugify

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
    def get(self,request, contract_slug):
        contract = get_list_or_404(Rates, contract = contract_slug)
        serializer = RatesSerializer(contract, many=True)
        return Response(serializer.data)

class CreateContract(APIView):
    def post(self, request):
        if request.method == 'POST': 
            obtained_name = request.POST.get('name') 
            obtained_date = request.POST.get('date') 
            Contract.objects.create(
                name = obtained_name,
                date = obtained_date 
            )
        return Response({
            "status": 'Success',
            "createdContractSlug": slugify(obtained_name)
        }) 
        
#try:
#    obj = Contract.objects.get(name= slugify(name))
#except Person.DoesNotExist:
#    obj = Person(first_name='John', last_name='Lennon', birthday=date(1940, 10, 9))
#    obj.save()