#This model.py file describes the database structure for anything related to products
from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField
    supplier = models.TextField()
    summary = models.TextField(default="Very Nice Product")