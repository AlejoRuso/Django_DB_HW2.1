from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'min_price':
        all_phones = Phone.objects.order_by('price')
    elif sort_by == 'max_price':
        all_phones = Phone.objects.order_by('-price')
    elif sort_by == 'name':
        all_phones = Phone.objects.order_by('name')
    else:
        all_phones = Phone.objects.order_by('id')
    context.setdefault('phones', all_phones)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    context = {
    'phone':
    Phone.objects.filter(slug__contains = slug).first()
    }
    return render(request, template, context)
