from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product, Customer, Command

# Create your views here.
def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

def gallery(request, category):
    # products = Product.objects.get(category=category)
    template = loader.get_template("gallery.html")
    context = {
        'category': category,
        # 'products': products,
    }
    return HttpResponse(template.render(context, request))

def product_page(request, product_name):
    product = Product.objects.get(product_name=product_name)
    template = loader.get_template("product_page.html")
    context = {
        'product': product,
    }
    return HttpResponse(template.render(context, request))

def customer_space(request, email):
    customer = Customer.objects.get(email=email)
    command = Command.objects.get(customer_email=email)
    template = loader.get_template("customer_space.html")
    context = {
        'customer': customer,
        'command': command,
    }
    return HttpResponse(template.render(context, request))