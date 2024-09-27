from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Maker(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    created_time = models.TimeField(auto_now_add=True, null=False, blank=False)
    updated_time = models.TimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Provider(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    

class Customer(models.Model):
    countries = (('SV', 'SV'),
                 ('GT', 'GT')   
                )
    full_name = models.CharField(max_length=250, null=False, blank=False)
    quote_code = models.CharField(max_length=15, null=False, blank=False)
    country_code = models.CharField(max_length=3, null=False, default='SV', choices=countries)
    active = models.BooleanField(default=True, null=False)
    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=True)


class Hdd_Capacity(models.Model):
    units = (
                ('GB', 'GB'),
                ('TB', 'TB')
            )

    value = models.FloatField(null=False, default=0.0)
    uom = models.CharField(max_length=2, null=False, blank=False, default="TB", choices=units )
    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.value} {self.uom}'
    
class Nas_Accessory_Category(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    active = models.BooleanField(null=False)
    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=True)


class Nas_Accessory(models.Model):
    #nas_model = ForeignKey()
    category = models.ForeignKey(Nas_Accessory_Category, on_delete= models.PROTECT)
    maker = models.ForeignKey(Maker, on_delete=models.PROTECT)
    model = models.CharField(max_length=25, null=False, blank=False)
    msrp = models.FloatField(null=False)
    active = models.BooleanField(null=False, default=True)
    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=True)

class Nas_Model(models.Model):
    model = models.CharField(max_length=12, null=False, blank=False)
    launch_year = models.PositiveSmallIntegerField(null=False)
    warranty_years = models.PositiveSmallIntegerField(null=False)
    is_rackable = models.BooleanField(null=False, default=False)
    has_redundant_ps = models.BooleanField(null=False, default=False)
    hdd_internal_slots = models.PositiveSmallIntegerField(null=False)
    ram_default = models.PositiveSmallIntegerField(null=False)
    ram_max = models.PositiveSmallIntegerField(null=False)
    ram_slots = models.PositiveSmallIntegerField(null=False)
    pci_slots_qty = models.PositiveSmallIntegerField(null=False)
    hdd_max_slots = models.PositiveSmallIntegerField(null=False)
    hdd_max_expansion_units_qty = models.PositiveSmallIntegerField(null=False)
    oneGb_nic_qty = models.PositiveSmallIntegerField(null=False)
    tenGb_compatible = models.BooleanField(null=False, default=False)
    tenGb_nic_qty = models.PositiveSmallIntegerField(null=False)
    m2_compatible = models.BooleanField(null=False, default=False)
    m2_internal_slots_qty = models.PositiveSmallIntegerField(null=False)
    msrp = models.FloatField(null=False, default=0.00)
    weight_in_pounds = models.FloatField(null=False, default=0.00)
    active = models.BooleanField(null=False, default=False)
    created_time = models.DateTimeField(auto_now_add=True,  null=False)
    updated_time = models.DateTimeField(auto_now=True, null=False)

    maker = models.ForeignKey(Maker,on_delete=models.PROTECT)
