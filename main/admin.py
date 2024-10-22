from django.contrib import admin
from .models import Product, Category, Promotion

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('product', 'discount', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
