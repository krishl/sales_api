from django.test import TestCase
from .models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.first_name = "First name"
        self.last_initial = "L"
        self.customer = Customer(first_name=self.first_name, last_initial=self.last_initial)

    def test_model_can_create_a_customer(self):
        """Test the customer model can create a customer."""
        old_count = Customer.objects.count()
        self.customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)