from django import http
from django.contrib import admin
from home.models import *
# Register your models here.
class cat(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,cat)

class product(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','catego']
    list_editable=['price','stock','catego','img']
    prepopulated_fields={'slug':('name',)}

admin.site.register(products,product)


