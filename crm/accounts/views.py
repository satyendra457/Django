from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'accounts/dashboard.html', context)

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
    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag_details')
        else:
            form = TagForm(instance=tag)
    context = {'tag': tag, 'form': form}
    return render(request, 'accounts/create_tag.html', context)

def DeleteTags(request, pk):
    tag = Tag.objects.get(id=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_details')
    context = {'tag': tag, 'name': "Tag"}
    return render(request, 'accounts/tag_delete.html', context)

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

def CustomerDetails(request, pk):
    customer = Customer.objects.get(id=pk)
    print("ccccccccccccc", customer)
    context = {'customer': customer}
    return render(request, 'accounts/customer_details.html', context)

def CreateCustomer(request):
    context = {}
    return render(request, 'accounts/customer_details.html', context=context)

def UpdateCustomer(request):
    context = {}
    return render(request, 'accounts/customer_details.html', context=context)

def DeleteCustomer(request):
    context = {}
    return render(request, 'accounts/customer_details.html', context=context)

