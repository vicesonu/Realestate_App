from rest_framework import serializers
from .models import listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main','slug')

class listingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields = '__all__'
        lookup_field = 'slug'