from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')#display at the admin
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')#In fields ko sirf dekh sakte ho, edit nahi kar sakte admin panel me.
    ordering = ('-date_joined',)#User list kis order me sort ho? -ve sign mtlb decending order
    filter_horizontal = ()
    list_filter = () #sidebar me checkbox filter aa jata.
    fieldsets = () #Admin form ke layout ko group karne ke liye use hota hai.

admin.site.register(Account, AccountAdmin)