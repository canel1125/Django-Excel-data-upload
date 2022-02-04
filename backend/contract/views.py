from datetime import date
from os import name
from django.http import Http404
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.defaultfilters import slugify
import json

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
            obtained_data = json.loads(request.body)

            obtained_name = obtained_data['name']
            obtained_date = obtained_data['date']
            obtained_rates = obtained_data['rates']
            

            #Consulto si el contrato ya fue creado, en caso de serlo solo agrego rates
            obj, created = Contract.objects.get_or_create(
            slug = slugify(obtained_name),
            defaults={'name': obtained_name, 'date': obtained_date},
            )

            rates_to_create = []
            for rate in obtained_rates:
                #Compruebo no ingresar valores vacios
                if "n.a." not in rate.values():
                    rateObject = Rates(
                    contract = obj,
                    origin = rate["POL"],
                    destination = rate["POD"],
                    currency = rate["Curr."],
                    twenty = rate["20'GP"],
                    forty = rate["40'GP"],
                    fortyhc = rate["40'HC"]
                )
                rates_to_create.append(rateObject)
        #Almaceno los rates todos juntos
        Rates.objects.bulk_create(rates_to_create)
            
        return Response({
            "status": 'Success',
            "createdContractSlug": slugify(obtained_name)
        }) 