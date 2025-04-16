from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')#where to store always tell
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#Also tell wht to do on delete(CASCADE=jb category delete hogi toh usse juda product b delete kr dena
    create_date = models.DateTimeField(auto_now_add=True)# when created
    modified_date = models.DateTimeField(auto_now=True)#when updated

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    def __str__(self):
        return self.product_name



class VariationManager(models.Manager):  #  Manager Django me ek interface hota hai jo tumhare model ke objects ko query karne ke liye use hota hai
    def color(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True) #Yahan super(VariationManager, self) ka matlab hai:"Apne parent class models.Manager ka filter() method call karo."
    def gender(self):
        return super(VariationManager, self).filter(variation_category='gender', is_active=True)

variation_category_choice = {
    ('color', 'color'),
    ('gender', 'gender'),
}
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()
    def __str__(self):
        return self.variation_value
