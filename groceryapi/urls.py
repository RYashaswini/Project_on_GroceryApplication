from django.urls import path
from .views import CustomerCreate,CustomerUpdate,UnitCreate,UnitUpdate,ProductCreate,ProductUpdate,OrderDetilCreate,OrderDetailUpdate,OrderCreate,OrderUpdate,ProductNN,ProductupdateNN,OrderdetailNN,orderdetailupdateNN,OrderNN,OrderupdateNN, DataCountGenerics,ListNN,ListupdateNN
urlpatterns = [
    path('create_customer/',CustomerCreate.as_view()),
    path('update_customer/<int:pk>/',CustomerUpdate.as_view()),

    path('create_unit/',UnitCreate.as_view()),
    path('update_unit/<int:pk>/',UnitUpdate.as_view()),

    path('create_product/',ProductCreate.as_view()),
    path('update_product/<int:pk>/',ProductUpdate.as_view()),

    path('create_orderdetail/',OrderDetilCreate.as_view()),
    path('update_orderdetail/<int:pk>/',OrderDetailUpdate.as_view()),

    path('create_order/',OrderCreate.as_view()),
    path('update_order/<int:pk>/',OrderUpdate.as_view()),

    path('product_nn/',ProductNN.as_view()),
    path('productupdate_nn/<int:pk>/',ProductupdateNN.as_view()),

    path('orderdetail_nn/',OrderdetailNN.as_view()),
    path('orderdetailupdate_nn/<int:pk>/',orderdetailupdateNN.as_view()),

    path('order_nn/',OrderNN.as_view()),
    path('orderupdate_nn/<int:pk>/',OrderupdateNN.as_view()),

    path('iterno/', DataCountGenerics.as_view()),

    path('listnn/',ListNN.as_view()),
    path('listupdatenn/<int:pk>/',ListupdateNN.as_view())

]