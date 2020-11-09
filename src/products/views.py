from django.shortcuts import render, redirect
from .forms import ProductForm, RawProductForm
from .models import Product


def product_update_view(request,id):
    initial_data = {
        'title': 'my title'
    }
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        print(1)
        redirect('products/'+str(id))
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


'''def product_create_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)'''
