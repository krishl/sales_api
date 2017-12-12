from rest_framework import serializers
from .models import Customer, Product, Cart

class ProductSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Product
        fields = ('id', 'name', 'description')

class CartSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Cart
        fields = ('id', 'customer', 'products')

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    cart = CartSerializer(many=False, read_only=True)    

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'first_name', 'last_initial', 'cart')