from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class Promotion(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.product.name} - {self.discount}% off"
