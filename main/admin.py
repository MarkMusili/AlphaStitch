from django.contrib import admin
from .models import Product, Category, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductImageInline(admin.TabularInline):  # or StackedInline for a vertical layout
    model = ProductImage
    extra = 1  # Number of extra blank image fields

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]  # Adds inline for images to the Product admin