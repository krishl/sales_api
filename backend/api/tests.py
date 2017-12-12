from django.test import TestCase
from .models import Customer, Product
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class CustomerModelTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.first_name = "First"
        self.last_initial = "L"
        self.customer = Customer(first_name=self.first_name, last_initial=self.last_initial)

    def test_model_can_create_a_customer(self):
        """Test the customer model can create a customer."""
        old_count = Customer.objects.count()
        self.customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)

class CustomerViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.customer_data = {'first_name': 'First', 'last_initial': 'L'}
        self.response = self.client.post(
            reverse('custCreate'),
            self.customer_data,
            format="json")

    def test_api_can_create_a_customer(self):
        """Test the api has customer creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_customer(self):
        """Test the api can get a given customer."""
        customer = Customer.objects.get()
        response = self.client.get(
            reverse('custDetails',
            kwargs={'pk': customer.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, customer)

    def test_api_can_update_customer(self):
        """Test the api can update a given customer."""
        customer = Customer.objects.get()        
        update_customer = {'first_name': 'Another', 'last_initial': 'K'}
        response = self.client.put(
            reverse('custDetails', kwargs={'pk': customer.id}),
            update_customer, format='json')
            
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_customer(self):
        """Test the api can delete a customer."""
        customer = Customer.objects.get()
        response = self.client.delete(
            reverse('custDetails', kwargs={'pk': customer.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class ProductModelTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.name = "Product"
        self.description= "Description"
        self.product = Product(name=self.name, description=self.description)

    def test_model_can_create_a_product(self):
        """Test the product model can create a product."""
        old_count = Product.objects.count()
        self.product.save()
        new_count = Product.objects.count()
        self.assertNotEqual(old_count, new_count)

class ProductViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.product_data = {'name': 'Name', 'description': 'Description'}
        self.response = self.client.post(
            reverse('prodCreate'),
            self.product_data,
            format="json")

    def test_api_can_create_a_product(self):
        """Test the api has product creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_product(self):
        """Test the api can get a given product."""
        product = Product.objects.get()
        response = self.client.get(
            reverse('prodDetails',
            kwargs={'pk': product.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, product)

    def test_api_can_update_product(self):
        """Test the api can update a given product."""
        product = Product.objects.get()        
        update_product = {'name': 'Name', 'description': 'Description'}
        response = self.client.put(
            reverse('prodDetails', kwargs={'pk': product.id}),
            update_product, format='json')
            
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_product(self):
        """Test the api can delete a product."""
        product = Product.objects.get()
        response = self.client.delete(
            reverse('prodDetails', kwargs={'pk': product.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)