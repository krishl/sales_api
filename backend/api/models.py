from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):
    """This class represents the customer model."""
    letters = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')
    first_name = models.CharField(max_length=255, blank=False, unique=False, validators=[letters])
    last_initial = models.CharField(max_length=1, blank=False, unique=False, validators=[letters])

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "%s" % self.first_name

class Cart(models.Model):
    """This class represents the cart model."""
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "%s" % self.customer

class Product(models.Model):
    """This class represents the product model."""
    name = models.CharField(max_length=255, blank=False, unique=False)
    description = models.CharField(max_length=1000, blank=False, unique=False)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "%s" % self.name