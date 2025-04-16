from django.shortcuts import render, get_object_or_404# get--> ye querry result laane me help krta hai
from .models import Product
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def store(request, category_slug=None): #=None mtlb diya toh use kro nhi diya toh rhne do
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)#Category table me se wo category fetch kar raha hai jo us slug se match karti ho
        products = Product.objects.filter(category=categories, is_available=True)#Fir Product table me gaye aur us fire category ke available Pokémon nikaale
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)  # those pages are stored here
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)  #those pages are stored here
        product_count = products.count()


    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)



#PRODUCT DETAILS
def product_detail(request, category_slug, product_slug):
    try:
        #.get--> cause aek hi product chaiye
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)  # Category naam ki ForeignKey me jao, fir uske slug ko compare karo/ fir product ka khud ka slug text kro
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()  # CartItem ka cart field (jo foreign key hai Cart pe), uska cart_id match karna chahiye _cart_id(request) ke return value se (jo ek session key hai).
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)



#SEARCH
def search(request):
    if 'keyword' in request.GET:  # check if keyword exist or not
        keyword = request.GET['keyword']  # assigning the value
        if keyword:
                                                                # we can't  use or operator without Q
            products = Product.objects.order_by('-create_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))  # searching products
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)
