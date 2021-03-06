from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=200, blank=True)
    created_at = models.DateField(auto_now_add=True)
