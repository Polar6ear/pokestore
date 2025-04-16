from django.db import models
from store.models import Product, Variation
# Create your models here.

class Cart(models.Model): #ye aek empty cart ke baare me btata hai
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):# ye btata hai ki cart me kon konse products hai aur unki quantity kya hai
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #yeh batata hai kaunsa product cart me add hua hai
    variations = models.ManyToManyField(Variation, blank=True)  # many product can have same variations
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #cart item kis cart se linked hai
    quantity = models.IntegerField() #kitne pieces add kiye hai
    is_active = models.BooleanField(default=True) #Agar item cart me hai (aur delete nahi hua), to True. Agar remove kar diya gaya, to False

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
