from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from core.models.product import Product
from core.models.orders import Order

class OrderView(View):
    def get(self,request):
        customer=request.session.get('customer')
        orders=Order.get_orders_by_customer(customer)
        print(orders)
        
        return render(request,'orders.html',{'orders':orders})
        

        
