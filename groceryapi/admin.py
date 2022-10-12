from django.contrib import admin
from .models import CustomerModel,UnitModel,ProductModel,OrderDetailModel,OrderModel

# Register your models here.

admin.site.register(CustomerModel)
admin.site.register(UnitModel)
admin.site.register(ProductModel)
admin.site.register(OrderDetailModel)
admin.site.register(OrderModel)
