from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def home(request):
    Categories = Category.objects.all()
    title = 'Home'
    default_image_url = '/media/default.jpg'
    context = {
        'title': title,
        'Categories': Categories,
        'default_image_url': default_image_url
    }

    return render(request, 'main/home.html', context)

def products(request):
    Categories = Category.objects.all()
    Products = Product.objects.all()
    title = 'Products'
    default_image_url = '/media/default.jpg'

    category_filter = request.GET.get('category')
    if category_filter:
        Products = Products.filter(category__id=category_filter)

    search_query = request.GET.get('search')
    if search_query:
        Products = Products.filter(name__icontains=search_query)


    context = {
        'title': title,
        'Categories': Categories,
        'Products': Products,
        'default_image_url': default_image_url,
        'selected_category': category_filter,
        'search_query': search_query,
    }
    return render(request, 'main/products.html', context)

def search_suggestions(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
        suggestions = []

        for product in products:
            suggestions.append({
                'name': product.name,
                'url': product.get_absolute_url(),
            })

        return JsonResponse(suggestions, safe=False)

    return JsonResponse([], safe=False)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'main/product_detail.html', {'product': product})