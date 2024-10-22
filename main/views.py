from django.shortcuts import render
from .models import Category

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