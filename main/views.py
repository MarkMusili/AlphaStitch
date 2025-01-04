from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm


def home(request):
    Categories = Category.objects.all()
    title = 'Alpha Stitch | Custom Shades, Blinds & Outdoor Accessories '
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
    title = 'Luxury Shades, Blinds,Camping Accessories & PVC Bags'
    default_image_url = '/media/default.jpg'

    category_filter = request.GET.get('category')
    if category_filter:
        Products = Products.filter(category__id=category_filter)
        if Products.count() == 0:
            return HttpResponseRedirect('https://alphastch.com/')


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
    title = f'{product.name} - High Quality {product.category.name} | Alpha Stitch'
    raw_features = product.features.split('\n')

    features = []
    for feature in raw_features:
        if ':' in feature:
            parts = feature.split(':', 1)
            features.append((parts[0].strip(), parts[1].strip()))
        else:
            features.append((feature.strip(), ''))

    context = {
        'title': title,
        'product': product,
        'features': features,
    }
    return render(request, 'main/product_detail.html', context)

def about(request):
    title = 'About Alpha Stitch | Quality Shades & Accessories in Cape Town'
    context = {
        'title': title,
    }
    return render(request, 'main/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('honeypot'):
                return HttpResponse("Bot detected. Submission blocked.", status=403)
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
            recipient_email = ['alphastitchsales@gmail.com']

            # Send the email
            send_mail(subject, body, email, recipient_email)

            return redirect('success')
    else:
        form = ContactForm()

    context = {'title': 'Contact Alpha Stitch | Get a Quote for Custom Orders', 'form': form}
    return render(request, 'main/contact.html', context)

def success(request):
    return render(request, 'main/success.html')
