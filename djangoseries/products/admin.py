from django.contrib import admin

# Register your models here.
from .models import Products
from .models import NewProducts
admin.site.register(Products)
#added an example of a real data value
admin.site.register(NewProducts)