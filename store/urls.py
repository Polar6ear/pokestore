from django.urls import path
from . import views
urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),#<type-->slug= lowercase, hyphenated version of name: variable ka naam hai jo URL se value capture karega, aur views.store function me as a parameter bhejega.>
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]