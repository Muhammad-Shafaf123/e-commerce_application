from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *





def store(request):
    producta = Product.objects.all()
    context = {'producta':Product}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
