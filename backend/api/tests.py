from django.test import TestCase
from .models import Customer
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
            reverse('create'),
            self.customer_data,
            format="json")

    def test_api_can_create_a_customer(self):
        """Test the api has customer creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)