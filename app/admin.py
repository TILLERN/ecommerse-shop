from django.contrib import admin
from .models import  *

class About_admin(admin.ModelAdmin):
    list_display=['article']

admin.site.register(About,About_admin)

class Social_media_admin(admin.ModelAdmin):
    list_display=['platform','link','username']

admin.site.register(Social_media,Social_media_admin)

class Phone_admin(admin.ModelAdmin):
    list_display=['number']

admin.site.register(Phone_number,Phone_admin)

class Email_admin(admin.ModelAdmin):
    list_display=['email_address']

admin.site.register(Email,Email_admin)

class Physical_address_admin(admin.ModelAdmin):
    list_display=['city','name','street','building','additional_information']

admin.site.register(Physical_address,Physical_address_admin)