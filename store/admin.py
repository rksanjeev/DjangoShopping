from django.contrib import admin
from .models import Product, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['is_active', 'in_stock', 'created_by', 'price', 'Category']
    prepopulated_fields = {'slug':('title',)}
    list_editable = ['price', 'in_stock']
    list_display = ('title', 'Category', 'price', 'in_stock', 'slug', 'created_by')

