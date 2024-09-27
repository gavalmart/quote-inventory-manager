from django.contrib import admin
from .models import Maker, Provider, Customer, Hdd_Capacity, Nas_Accessory, Nas_Accessory_Category, Nas_Model


# Register your models here.
admin.site.register(Maker)
admin.site.register(Provider)
admin.site.register(Customer)
admin.site.register(Hdd_Capacity)
admin.site.register(Nas_Model)
admin.site.register(Nas_Accessory)
admin.site.register(Nas_Accessory_Category)
