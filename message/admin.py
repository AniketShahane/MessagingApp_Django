from django.contrib import admin
from .models import message
# Register your models here.

class messageAdmin(admin.ModelAdmin):
    list_display = ('id','sender', 'receiver')
    list_display_links = ('id', 'sender')
    list_filter = ('sender', 'receiver')
    list_perpage = 25

admin.site.register(message, messageAdmin)
