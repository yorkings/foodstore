from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50) 
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created_at =models.DateTimeField(default=datetime.now)
class Cart(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
