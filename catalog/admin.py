from django.contrib import admin

# Register your models here.

from .models import Categorie, Subcategorie, Product, ProductImage
from django.contrib.auth.models import Group


class ProductImageInline(admin.TabularInline):
    model = ProductImage



class ProductAdminMaster(admin.ModelAdmin):
    # model = Product
    inlines = [ProductImageInline]


admin.site.unregister(Group)

admin.site.register(Product, ProductAdminMaster)
# admin.site.register(AttributeInline, ProductAdminMaster)
admin.site.register(Categorie, )
admin.site.register(Subcategorie, )