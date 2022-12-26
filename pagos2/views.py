from django.shortcuts import render
from .models import Services, Payment_user,Expired_payments
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import ServicesSerializer,PaymentUserSerializer,ExpiredPaymentsSerializer
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from datetime import datetime
from rest_framework import filters,status
from rest_framework.viewsets import ModelViewSet

class ServicesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ServicesSerializer
    throttle_scope = 'view_others'

    def get_queryset(self):
        return Services.objects.all()
   
    def get_object(self, queryset=None, **kwargs):
        item_services= self.kwargs.get('pk')
        return get_object_or_404(Services, id=item_services)


       

