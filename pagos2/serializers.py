from rest_framework import serializers
from .models import Services,Expired_payments,Payment_user

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ExpiredPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = '__all__'
        read_only_fields = ["Id","User_id","Service_id","Amount","PaymentDate","ExpirationDate"]

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
        read_only_fields = ["Id","Payment_user_id","Penalty_fee_amount"]
    