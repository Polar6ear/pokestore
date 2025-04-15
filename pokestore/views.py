from django.http import HttpResponse #choti lines print krni ho toh use krte hai
from django.shortcuts import render
from store.models import Product
def home(request): #jb koi user/browser django aap ko visit krta hai toh aek request object bnta hai
                    #jisme puri info hoti hai ex: cookies, url, post/get etc
    products = Product.objects.all().filter(is_available=True)#m.objects--> model ke uper operations krne deta hai
                                                            #.filters--> ye bolta hai vhi do jo available ho
    context = {
        'products': products,
    }
    #return HttpResponse('home page')
    return render(request, 'home.html', context) #render --> jb kisi page ka html template dikhana ho
                                                                #ye 3 arguments leta hai request, template-name, datafield