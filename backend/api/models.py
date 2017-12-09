from django.db import models

class Customer(models.Model):
    """This class represents the customer model."""
    first_name = models.CharField(max_length=255, blank=False, unique=False)
    last_initial = models.CharField(max_length=1, blank=False, unique=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "%s the place" % self.first_name