from django.db import models
from django.urls import reverse
import json
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', default='default.jpg', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', default='default.jpg',null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    features = models.TextField(null=True, blank=True, help_text="Store multiple descriptions separated by newlines")

    def get_features(self):
        if self.features:
            return self.features.split('\n')
        return []

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Image for {self.product.name}"

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()  # Update the timestamp on each save
        super().save(*args, **kwargs)