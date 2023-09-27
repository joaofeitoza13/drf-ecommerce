from django.contrib import admin  # noqa: F401

from .models import Brand, Category, Product, ProductLine


class ProductLineInline(admin.TabularInline):
    model = ProductLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductLine)
