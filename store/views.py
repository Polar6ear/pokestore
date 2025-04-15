from django.shortcuts import render, get_object_or_404# get--> ye querry result laane me help krta hai
from .models import Product
from category.models import Category
# Create your views here.
def store(request, category_slug=None): #=None mtlb diya toh use kro nhi diya toh rhne do
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)#Category table me se wo category fetch kar raha hai jo us slug se match karti ho
        products = Product.objects.filter(category=categories, is_available=True)#Fir Product table me gaye aur us fire category ke available Pokémon nikaale
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()


    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)



#PRODUCT DETAILS
def product_detail(request, category_slug, product_slug):
    try:
        #.get--> cause aek hi product chaiye
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)#Category naam ki ForeignKey me jao, fir uske slug ko compare karo/ fir product ka khud ka slug text kro
    except Exception as e:
        raise e
    context = {
        'single_product': single_product
    }
    return render(request, 'store/product_detail.html', context)