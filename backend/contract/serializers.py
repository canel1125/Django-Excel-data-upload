from rest_framework import serializers

from .models import Contract, Rates

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields =(
            'id',
            'name',
            'date',
            'slug'
        )


class RatesSerializer(serializers.ModelSerializer):
    contract = serializers.SlugRelatedField(
        read_only=True,
        slug_field='slug'
    )
    class Meta:
        model = Rates
        fields =(
            'id',
            'contract',
            'origin',
            'destination',
            'currency',
            'twenty',
            'forty',
            'fortyhc'
        )