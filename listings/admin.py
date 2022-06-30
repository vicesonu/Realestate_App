from django.contrib import admin
from .models import listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'price', 'list_date')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(listing, ListingAdmin)
