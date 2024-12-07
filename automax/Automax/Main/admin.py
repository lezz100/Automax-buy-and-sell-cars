from django.contrib import admin
from .models import Listing,LikedListing

class ListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'vin')

class LikedListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )


admin.site.register(Listing, ListingAdmin)
admin.site.register(LikedListing, LikedListingAdmin)

