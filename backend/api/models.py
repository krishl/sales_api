from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):
    """This class represents the customer model."""
    letters = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')
    first_name = models.CharField(max_length=255, blank=False, unique=False, validators=[letters])
    last_initial = models.CharField(max_length=1, blank=False, unique=False, validators=[letters])

    def __str__(self):
        """Return a human readable representation of the customer instance."""
        return self.first_name

class Product(models.Model):
    """This class represents the product model."""
    name = models.CharField(max_length=255, blank=False, unique=False)
    description = models.CharField(max_length=255, blank=False, unique=False)

    def __str__(self):
        """Return a human readable representation of the product instance."""
        return self.name

class Cart(models.Model):
    """This class represents the cart model."""
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        """Return a human readable representation of the cart instance."""
        return self.customer