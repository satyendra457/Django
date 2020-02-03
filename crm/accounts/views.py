from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def TagsDetails(request):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'accounts/tag_details.html', context)

def CreateTags(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_details')
    context = {'form': form}
    return render(request, 'accounts/create_tag.html', context)

def UpdateTags(request, pk):
    context = {}
    return render(request, 'accounts/create_tag.html', context)

def DeleteTags(request, pk):
    context = {}
    return render(request, 'accounts/create_tag.html', context)

def ProductDetails(request):
    products = Product.objects.all()
    context = {
                'products': products
              }
    return render(request, 'accounts/product.html', context)

def CreateProduct(request):
    forms = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_details')
    context = {'forms': forms}
    return render(request, 'accounts/create_product.html', context)

def UpdateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid:
            form.save()
            return redirect('product_details')
        else:
            form = ProductForm(instance=product)
    context = {'product': product, 'forms': form}
    return render(request, 'accounts/create_product.html', context)

def DeleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_details')
    context = {'product': product, 'name': "Product"}
    return render(request, 'accounts/delete.html', context)
