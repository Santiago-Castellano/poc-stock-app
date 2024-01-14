from django.contrib import admin
from .models import Product, Service, ServiceProduct
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'price', 'total_uses','price_per_use',)
    search_fields = ('name',)
    list_filter = ('uses_in_services__service',)


class ServiceProductInline(admin.TabularInline):
    model = ServiceProduct
    extra = 1
    autocomplete_fields = ['product']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('cost', 'price')
    list_display = ('name', 'cost', 'price')
    inlines = [ServiceProductInline]

