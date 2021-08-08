# Create your models here.
from datetime import datetime

from django.utils import timezone
from django.db import models, connection 


cursor = connection.cursor()


class FoodCategory(models.Model):
    """ Represents food categories """

    category_name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Food Category"

class FoodDetails(models.Model):
    """ Represents food details """

    category_id = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name="category_id")
    food_name = models.CharField(max_length=64)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Food Details"

class CustomerDetails(models.Model):
    """ Represents customer details """

    cust_email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Customer Details"

class CustOrderStatus(models.Model):
    """ Represents order status """

    cust_id = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, related_name="cust_id")
    order_status = models.CharField(max_length=64, null=True, blank=True)
    order_address = models.CharField(max_length=64, null=True, blank=True)
    bill_amount = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Customer Order Status"


class CustOrderSelection(models.Model):    
    """ Represents food ordered """

    order_id = models.ForeignKey(CustOrderStatus, on_delete=models.CASCADE, related_name="order_id")
    food_id = models.ForeignKey(FoodDetails, on_delete=models.CASCADE, related_name="food_id")  
    food_qty = models.IntegerField()

    class Meta:
        verbose_name_plural = "Customer Order Selection"