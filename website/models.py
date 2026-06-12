from django.db import models

# Create your models here.

class Pray(models.Model):

    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # Keeps track of when it was sent

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"