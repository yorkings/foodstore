from django.contrib import admin
from .models import *
# Register your models here.
class focus(admin.ModelAdmin):
    list_display=['product','price']
admin.site.register(Product,focus)
admin.site.register(Cart)