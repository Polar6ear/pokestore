from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)#to auto generate slug
    description = models.TextField(max_length=255, blank=True)  #blank=True-->optional
    cat_image = models.ImageField(upload_to='photos/categories', blank=True) #upload_to--> when upload where to go
                                                        #since we are using image we need to instll Pillow

    class Meta:
        verbose_name = 'category'               #sb kux plural me hota hai toh shi krne ko ye kiya hai
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])#link bnayega is slug ke base pr
                                                        #agrs=order base value pass krta hai
                                                        #kwargs=name base
    def __str__(self): #string rep of the model
        return self.category_name