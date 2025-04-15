from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { #automatically generate slug
        'slug': ('category_name',)#since it's a tuple
    }
    list_display = ('category_name', 'slug')
admin.site.register(Category, CategoryAdmin)#register the category

