from rest_framework import serializers

from .models import Contract, Rates

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields =(
            'name',
            'date',
            'slug'
        )


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields =(
            'contract',
            'origin',
            'destination',
            'currency',
            'twenty',
            'forty',
            'fortyhc'
        )