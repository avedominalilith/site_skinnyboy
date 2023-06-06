from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'pools/index.html', {})

def about(request):
    return render(request, 'pools/about.html', {})

def products(request):
    return render(request, 'pools/products.html', {})

def popular(request):
    return render(request, 'pools/popular.html', {})

def shops(request):
    return render(request, 'pools/shops.html', {})

