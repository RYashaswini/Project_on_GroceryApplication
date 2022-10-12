from rest_framework import serializers 

from .models import CustomerModel,UnitModel,ProductModel,OrderDetailModel,OrderModel

#------Independent Serializer-----

class CustomerSeializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ['cust_id','customer_name','phone_number','city']

class UnitSeializer(serializers.ModelSerializer):
    class Meta:
        model = UnitModel
        fields = ['unit_id','unit_name']

#---------Nested Serializer-------

class ProductSeializer(serializers.ModelSerializer):
    unit=serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        fields = ['prod_id','product_name','unit_id','unit','product_price',]

    def get_unit(self, obj):
        data = UnitModel.objects.filter(unit_name=obj.unit_id).values()
        return data


class OrderSeializer(serializers.ModelSerializer):
    customer =serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = ['order_id','order_no','customer','cust_id','order_date','total_amount','product_desc']

    def get_customer(self, obj):
        data = CustomerModel.objects.filter(customer_name=obj.cust_id).values()
        return data

class OrderDetailSeializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()

    class Meta:
        model = OrderDetailModel
        fields = ['orderdetail_id','order_id','prod_id','unit_ordered','price_ordered','quantity_ordered','total_amount_ordered','order']

    def get_order(self, obj):
        data = OrderModel.objects.filter(order_no=obj.order_id).values()
        return data

class NestlistSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    customer =serializers.SerializerMethodField()
    

    class Meta:
        model = OrderModel
        fields = ['order_id','order_no','customer','order_date','total_amount','product_desc','details']

    def get_details(self, obj):
        data = OrderDetailModel.objects.filter(order_id=obj.order_id).values()
        return data
    
    def get_customer(self, obj):
        data = CustomerModel.objects.filter(customer_name=obj.cust_id).values()
        return data

    


#------Non Nested Serializer-------

class ProductSeializerNN(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['prod_id','product_name','unit_id','product_price']

class OrderDetailSeializerNN(serializers.ModelSerializer):
    class Meta:
        model = OrderDetailModel
        fields = ['orderdetail_id','order_id','prod_id','unit_ordered','price_ordered','quantity_ordered','total_amount_ordered']


class OrderSeializerNN(serializers.ModelSerializer):
  
    class Meta:
        model = OrderModel
        fields = ['cust_id','order_id','order_no','order_date','total_amount','product_desc']

    # def validate(self, data):

    #     if (data.get('total_amount')) <= 0:
    #        raise serializers.ValidationError({'total_amount':'Total amount cannot be empty'})
    
    #     return data




class DataCount(serializers.ModelSerializer):
    iter_no = serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = ['order_id','iter_no']

    def get_iter_no(self, obj):
        try:
            data = OrderModel.objects.last()
            values =data.order_id + 1
            return "OR%0003d" % values
        except:
            return "OR0001"




