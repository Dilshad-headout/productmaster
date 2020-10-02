from django.contrib import admin
from .models import Product,BusinessOwner,ListingMember

# admin.site.register(NewClass)

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    # fields = ['title','description']  #to show only the gven content inside.
    list_display = ['category_name','tgid','product_name'] #display contents outside
    list_filter = ['category_name','tgid','product_name']
    search_fields = ['category_name']


@admin.register(BusinessOwner)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['business_owner', 'product']

@admin.register(ListingMember)
class ListingMemberAdmin(admin.ModelAdmin):
    list_display = ['name']