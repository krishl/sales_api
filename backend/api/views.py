from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomerSerializer
from .models import Customer

class CreateCustomerView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_customer_create(self, serializer):
        """Save the post data when creating a new customer."""
        serializer.save()