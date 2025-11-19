from django.db import models

# Create your models here.
#once changes are made to models.py you run python manage.py makemigrations
class Products(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField
    supplier = models.TextField()
    summary = models.TextField(default="Very Nice Product")

class NewProducts(models.Model):
    title = models.CharField(max_length=100) #charfield requires maxlength
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)