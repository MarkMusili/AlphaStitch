from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm


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
    Categories = Category.objects.all().order_by('id')
    Products = Product.objects.all().order_by('id')
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

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    raw_features = product.features.split('\n')

    features = []
    for feature in raw_features:
        if ':' in feature:
            parts = feature.split(':', 1)
            features.append((parts[0].strip(), parts[1].strip()))
        else:
            features.append((feature.strip(), ''))

    context = {
        'product': product,
        'features': features,
    }
    return render(request, 'main/product_detail.html', context)

def about(request):
    title = 'About'
    context = {
        'title': title,
    }
    return render(request, 'main/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Collect form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            product = form.cleaned_data['product']
            message = form.cleaned_data['message']

            # Compose the email content
            subject = f"Quote Request from {first_name} {last_name}"
            body = (
                f"Product Selected: {product.name}\n\n"
                f"Name: {first_name} {last_name}\n"
                f"Email: {email}\n"
                f"Phone Number: {phone_number}\n\n"
                f"Message:\n{message}"
            )
            recipient_email = ['alphastitchsales@gmail.com'] # Replace here with your alpha-stitch email

            # Send the email
            send_mail(subject, body, email, recipient_email)

            return redirect('success')
    else:
        form = ContactForm()

    context = {'title': 'Contact', 'form': form}
    return render(request, 'main/contact.html', context)

def success(request):
    return render(request, 'main/success.html')
