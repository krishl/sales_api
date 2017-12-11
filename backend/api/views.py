from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomerSerializer, ProductSerializer
from .models import Customer, Product

class CreateCustomerView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_customer_create(self, serializer):
        """Save the post data when creating a new customer."""
        serializer.save()

class CustomerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CreateProductView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_customer_create(self, serializer):
        """Save the post data when creating a new customer."""
        serializer.save()

class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer