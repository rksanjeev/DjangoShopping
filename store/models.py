from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='creator', on_delete=models.DO_NOTHING)  
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created','in_stock',)
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])


    
    def __str__(self) -> str:
        return self.title




