from django.shortcuts import render

from appproduct.models import Product

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[:8]
    return render(request, "core/frontpage.html", {'products': products})
