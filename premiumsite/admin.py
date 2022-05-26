from django.contrib import admin

# Register your models here.
from premiumsite.forms import ProfileForm
from premiumsite.models import *


# Define the admin class
# @admin.register(Iphone)
class PhoneAdmin(admin.ModelAdmin):
    pass
    list_display = [
        'model_phone', 'memory_phone', 'colors_phone',
        'region_phone', 'price_phone', 'availability_phone',
        'new_or_used', 'created_at',
        'update_at']

    search_fields = ['model_phone']
    # form = ProfileForm
    list_filter = ['model_phone', 'memory_phone', 'colors_phone']


# Register the Admin classes for Book using the decorator

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    pass


# Register the Admin classes for BookInstance using the decorator

@admin.register(AllColors)
class AllColorsAdmin(admin.ModelAdmin):
    pass


# @admin.register(UsedPhones)
# class UsedAdmin(admin.ModelAdmin):
#     pass


@admin.register(iMac)
class iMacAdmin(admin.ModelAdmin):
    pass


@admin.register(MacBook)
class MacBookAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


# @admin.register(Apple)
class iPhoneAdmin(admin.ModelAdmin):
    list_display = ('iphone_name',)
    search_fields = ('model_phone',)


admin.site.register(Phone, PhoneAdmin)
admin.site.register(iPhone, iPhoneAdmin)

'''class categories(admin.ModelAdmin):
    list_display = ('title', 'get_parents', 'when')'''
