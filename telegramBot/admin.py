from django.contrib import admin

from telegramBot.forms import ProfileForm
from telegramBot.models import *


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile','text','created_at')

    '''def get_queryset(self, request):
        return'''

