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

    # def update(self, instance, validated_data):
    #     product = Product.objects.get(name=validated_data.get('name'))       
    #     instance.products.add(product)
    #     instance.save()
    #     return instance

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    cart = CartSerializer(many=False, read_only=True)    

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Customer
        fields = ('id', 'first_name', 'last_initial', 'cart')

    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        Cart.objects.create(customer=customer)
        return customer
