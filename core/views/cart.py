from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from core.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from core.models import Product

class Cart(View):
    def get(self, request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)

        return render(request, "cart.html",{'products':products})
