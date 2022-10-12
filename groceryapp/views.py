
from django.contrib import messages
from urllib import response
from django.shortcuts import render,redirect
from django.conf import settings
import requests
from django.http import HttpResponse
import json
from django.db import transaction

url = settings.URL

# @transaction.atomic
def create_order_detail(request):

    if request.method == 'POST':
    
        name =  request.POST['ddlCustomer']
        order_no =  request.POST['txtOrderNo']
        ord_date = request.POST['txtOrderDate']
        total_amount = request.POST['txtTotalAmt']
        product_desc = request.POST['commentDescription']
    
        
        data = {'cust_id': name,'order_no': order_no,'order_date': ord_date, 'total_amount' : total_amount, 'product_desc' : product_desc}
       
            
        try:
            print("00000000000000000000000000000000000000000000000000")
            hiddenArray = request.POST['hiddenArray']
            json_object = json.loads(hiddenArray)
            print(type(hiddenArray))
            
            print(json_object)
            print(type(json_object))

              
        
            with transaction.atomic():
                response = requests.post('{url}/api/order_nn/'.format(url=url),data=data)
                value = response.text
                print(value)
                print('------value---------')
                json_data = json.loads(value)
                get_order_id = json_data['order_id']

            for hidden_data in json_object:

                prod = hidden_data['prod_id'] 
                unit = hidden_data['unit_ordered'] 
                price = hidden_data['price_ordered'] 
                qty = hidden_data['quantity_ordered'] 
                t_amt = hidden_data['total_amount_ordered'] 

                
                table_data = {
                    "order_id" : get_order_id,
                    "prod_id" : prod,
                    "unit_ordered" : unit,
                    "price_ordered" : price,
                    "quantity_ordered" : qty,
                    "total_amount_ordered" : t_amt,
                }
                
                response1 = requests.post('{url}/api/orderdetail_nn/'.format(url=url),data=table_data)
                print(response1.text)
            status_code_list = [200,302,201]
            if response1.status_code in status_code_list:
                messages.success(request,"successfully saved")
                return redirect('order')
            else:
                messages.error(request,"Validation Error")
                return redirect('create_order_details')
        except:
            messages.error(request,"checking atomic transaction")
            return redirect('create_order_details')

        # else:
        #     messages.error(request,"Validation Error")
            return redirect('create_order_details')
    else:
        print("-------------------create-------------")
        customerdata = requests.get('{url}/api/create_customer/'.format(url=url)).json()
        productdata = requests.get('{url}/api/product_nn/'.format(url=url)).json()
        productdetail = requests.get('{url}/api/create_orderdetail/'.format(url=url)).json()
        #print("productdet :",productdetail)
        #print("customer:",customerdata)
        #print("product:",productdata)
        return render(request,'order_detail.html',{'customerdata' : customerdata, 'productdata': productdata, 'productdetail' : productdetail })

def orders(request):
    print("-------------------list--------------")
    response = requests.get('{url}/api/create_order/'.format(url=url)).json()
    #print(response)
    return render(request,'order.html',{'response' : response})

def delete_order(request,order_id):
    response_delete=requests.delete("{url}/api/orderupdate_nn/{pk}/".format(url=url, pk=order_id))
    print(response_delete.text)
    messages.success(request,("Order deleted successfully"))
    return redirect('order')


def update_orders(request,order_id):

    if request.POST.get('btnSaveorder','') == 'SaveOrder':
        t_amount = request.POST['txtTotalAmt']
        if float(t_amount) > 0.00:
    
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            
            del_data = requests.delete('{url}/api/listupdatenn/{pk}/'.format(url=url,pk=order_id))
        
            print("deleteorder:",del_data.text)
    
            name =  request.POST['ddlCustomer']
            order_no =  request.POST['txtOrderNo']
            ord_date = request.POST['txtOrderDate'] 
            total_amount = request.POST['txtTotalAmt']
            product_desc = request.POST['commentDescription']
            hiddenArray = request.POST['hiddenArray']
            json_object = json.loads(hiddenArray)


            data = {'cust_id': name,'order_no': order_no,'order_date': ord_date, 'total_amount' : total_amount, 'product_desc' : product_desc}
            response = requests.post('{url}/api/order_nn/'.format(url=url),data=data) 

            print(type(hiddenArray))
            print(json_object)
            print(type(json_object))

            value = response.text
            print(value)
            print('------value---------')
            json_data = json.loads(value)
            get_order_id = json_data['order_id']
            
            for hidden_data in json_object:
                
                prod = hidden_data['prod_id'] 
                unit = hidden_data['unit_ordered'] 
                price = hidden_data['price_ordered'] 
                qty = hidden_data['quantity_ordered'] 
                t_amt = hidden_data['total_amount_ordered'] 

                table_data = {
                    "order_id" : get_order_id,
                    "prod_id" : prod,
                    "unit_ordered" : unit,
                    "price_ordered" : price,
                    "quantity_ordered" : qty,
                    "total_amount_ordered" : t_amt,
                }
                response1 = requests.post('{url}/api/orderdetail_nn/'.format(url=url),data=table_data) 
            
            print(response1)
            print(response1.text)        
            messages.success(request,("Order added successfully"))
            print('SUCCESS')
            return redirect('order')
        else:
            messages.error(request,"Validation Error")
            return redirect('create_order_details')
            
    elif request.POST.get('hiddenvalue','') == 'EditOrder':
        if_value = request.POST['hiddenvalue']
        print("check:",if_value)
        order_list = requests.get('{url}/api/listupdatenn/{pk}/'.format(url=url,pk=order_id)).json()
        productdata = requests.get('{url}/api/product_nn/'.format(url=url)).json()
        print("---------order_list--------------")
        print(order_list)
       
       
        return render(request,'order_detail.html',{'order_list' : order_list, 'if_value' : if_value,'productdata' :productdata})
   
    else:
        print("-------redirect---------")
        return render(request,'order_detail.html')


#-----------Master data-------  
def details(request):
    unit_data=requests.get('{url}/api/create_unit/'.format(url=url)).json() 
    return render(request,'details.html',{'unit_data':unit_data})

def create_customer(request):
    if request.method=='POST':
        name=request.POST['txtCustName']
        address=request.POST['txtCustCity']
        phone_number=request.POST['txtPhNo']
        print('------------customer-------------')
        data={
            'customer_name':name,
            'city':address,
            'phone_number':phone_number,
            }
        response=requests.post('{url}/api/create_customer/'.format(url=url), data=data)
        print(data)
        print(response.text)
        messages.success(request,("customer data added successfully"))
        return redirect('create_customer')
    else:
        print('-------------------------else customer-------------')
        cust_data=requests.get('{url}/api/create_customer/'.format(url=url)).json()     
        print(cust_data)   
        return render(request,'customer.html',{'cust_data': cust_data})

def updatecust(request,cust_id):
    print("--------******************************************")
    if request.method=='POST':
        name=request.POST['txtCustName']
        address=request.POST['txtCustCity']
        phone_number=request.POST['txtPhNo']
        print('------------customer-------------')
        data={
            'customer_name':name,
            'city':address,
            'phone_number':phone_number,
            }
        print('************************************************')
        print('update data:', data)
        response = requests.put('{url}/api/update_customer/{pk}/'.format(pk=cust_id,url=url), data=data)
        print(response)
        print(response.text)
        return redirect('create_customer')
    return render(request,'customer.html',{'response' : response})

def deletecust(request,cust_id):
    del_cust = requests.delete('{url}/api/update_customer/{pk}/'.format(pk=cust_id,url=url))
    return redirect('create_customer')



def create_product(request):
    if request.method=='POST':
        product_name=request.POST['txtProName']
        price=request.POST['txtProPrice']
        unit=request.POST['ddlUnitName']
        print('------------product-------------')
        data={
            'product_name':product_name,
            'unit_id':unit,
            'product_price':price,
            }
        response=requests.post('{url}/api/product_nn/'.format(url=url), data=data)
        print(data)
        print(response)
        messages.success(request,("Product data added successfully"))
        return redirect('create_product')
    else:
        print('-------------------------product else-------------')
        prod_data=requests.get('{url}/api/create_product/'.format(url=url)).json()   
        unit_data=requests.get('{url}/api/create_unit/'.format(url=url)).json()        
        print(prod_data)    
        print(unit_data)    
        return render(request,'products.html',{'prod_data':prod_data,'unit_data':unit_data})

def updateprod(request,prod_id):
    print("--------******************************************")
    if request.method=='POST':
        product_name=request.POST['txtProName']
        price=request.POST['txtProPrice']
        unit=request.POST['ddlUnitName']
        print('------------product-------------')
        data={
            'product_name':product_name,
            'unit_id':unit,
            'product_price':price,
            }
        print('************************************************')
        print('update data:', data)
        response = requests.put('{url}/api/update_product/{pk}/'.format(pk=prod_id,url=url), data=data)
        print(response)
        print(response.text)
        return redirect('create_product')
    return render(request,'products.html',{'response' : response})

def deleteprod(request,prod_id):
    del_cust = requests.delete('{url}/api/update_product/{pk}/'.format(pk=prod_id,url=url))
    return redirect('create_product')

def create_unit(request):
    if request.method=='POST':
        unit=request.POST['txtUnitName']
        print('------------unit-------------')
        data={
            'unit_name':unit,
            }
        response=requests.post('{url}/api/create_unit/'.format(url=url), data=data)
        print(data)
        print(response.text)
        messages.success(request,("Unit added successfully"))
        return redirect('create_unit')
    else:
        print('-------------------------unit else-------------')
        unit_data=requests.get('{url}/api/create_unit/'.format(url=url)).json()        
        return render(request,'unit.html',{'unit_data':unit_data})

def updateunit(request,unit_id):
    print("--------******************************************")
    if request.method=='POST':
        unit=request.POST['txtUnitName']
        print('------------unit-------------')
        data={
            'unit_name':unit,
            }
        response = requests.put('{url}/api/update_unit/{pk}/'.format(pk=unit_id,url=url), data=data)
        print(data)
        print(response.text)
        return redirect('create_unit')
    return render(request,'unit.html',{'response' : response})

def deleteunit(request,unit_id):
    del_unit = requests.delete('{url}/api/update_unit/{pk}/'.format(pk=unit_id,url=url))
    return redirect('create_unit')














