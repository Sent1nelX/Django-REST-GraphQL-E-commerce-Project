from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def IndexView(request):
       products = Product.objects.all()


       context = {
              'products': products
       
       }
       return render(request, 'index.html', context)


def ProductDetailView(request, slug):
       product = get_object_or_404(Product, slug=slug)

       context = {
              'product': product
       }
       return render(request, 'product_detail.html', context)