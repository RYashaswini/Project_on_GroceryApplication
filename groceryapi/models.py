from statistics import mode
from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    cust_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name

class UnitModel(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=10)

    def __str__(self):
        return self.unit_name

class ProductModel(models.Model):
    prod_id = models.AutoField(primary_key=True)
    unit_id = models.ForeignKey(UnitModel,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product_name

class OrderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_no = models.CharField(max_length=150)
    cust_id = models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    order_date = models.CharField(max_length=500)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    product_desc = models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.order_no

class OrderDetailModel(models.Model):
    orderdetail_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(OrderModel,on_delete=models.CASCADE,null=True,blank=True)
    prod_id = models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True,blank=True)
    unit_ordered = models.CharField(max_length=20)
    price_ordered = models.DecimalField(max_digits=50, decimal_places=2)
    quantity_ordered = models.IntegerField()
    total_amount_ordered = models.DecimalField(max_digits=50, decimal_places=2)

  



