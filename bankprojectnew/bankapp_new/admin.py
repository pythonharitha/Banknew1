from django.contrib import admin
from .models import District, Branch, Customer, Account_type

# Register your models here.

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Account_type)