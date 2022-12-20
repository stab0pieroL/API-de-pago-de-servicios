from rest_framework import serializers
from .models import Services,Expired_payments,Payment_user

class Pago2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Services,Expired_payments,Payment_user
        fields = '__all__'
        read_only_fields = '__all__',