from django.urls import path
from groceryapp import views

urlpatterns=[
    path('',views.create_order_detail,name="create_order_details"),
    path('order/',views.orders,name="order"),
    path('details/',views.details,name="details"),
    path('delete_order/<int:order_id>/',views.delete_order,name="delete_order"),
    path('update_order/<int:order_id>/',views.update_orders ,name='update_order'),
    
    path('create_product/',views.create_product,name="create_product"),
    path('create_unit/',views.create_unit,name="create_unit"),
    path('create_customer/',views.create_customer,name="create_customer"),

    path('updatecust/<int:cust_id>/',views.updatecust,name="updatecust"),
    path('deletecust/<int:cust_id>/',views.deletecust,name="deletecust"),

    path('updateunit/<int:unit_id>/',views.updateunit,name="updateunit"),
    path('deleteunit/<int:unit_id>/',views.deleteunit,name="deleteunit"),

    path('updateprod/<int:prod_id>/',views.updateprod,name="updateprod"),
    path('deleteprod/<int:prod_id>/',views.deleteprod,name="deleteprod"),
]
