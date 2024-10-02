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

    def __str__(self) -> str:
        return self.name


class Nas_Model(models.Model):
    warranty_period_choices = (
                            (2,2), (3,3), (5,5)
                        )
    
    cpu_quantity_choices = (
                        (1,1), (2,2), (3,3), (4,4)
                    )
    
    cores_per_cpu_choices = (
                                (2,2), (4,4), (6,6), (8,8), (10,10), (12,12)
                            )
    oneGb_ports_qty_choices = (
                                (1,1), (2,2), (3,3), (4,4)
                              )

    hdd_slots_choices = (
                            (1,1), (2,2), (4,4), (5,5), (6,6), (8,8), (12,12)
                        )


    maker = models.ForeignKey(Maker,on_delete=models.PROTECT)
    model = models.CharField(max_length=12, null=False, blank=False)
    launch_year = models.PositiveSmallIntegerField(null=False)
    warranty_years = models.PositiveSmallIntegerField(null=False, default=2, choices=warranty_period_choices)
    cpu_model = models.CharField(max_length=25, null=True)
    cpu_qty = models.PositiveBigIntegerField(null=False, default=1, choices=cpu_quantity_choices)
    cores_per_cpu = models.PositiveBigIntegerField(null=False, default=1, choices=cores_per_cpu_choices)
    weight_in_pounds = models.FloatField(null=False, default=0.00)
    msrp = models.FloatField(null=False, default=0.00)
    is_rackable = models.BooleanField(null=False, default=False)
    has_redundant_ps = models.BooleanField(null=False, default=False)
    pci_slots_qty = models.PositiveSmallIntegerField(null=False, default=0)
    m2_compatible = models.BooleanField(null=False, default=False)
    m2_internal_slots_qty = models.PositiveSmallIntegerField(null=False, default=0)
    ram_default_GB = models.PositiveSmallIntegerField(null=False, default=2)
    ram_max_GB = models.PositiveSmallIntegerField(null=False, default=0)
    ram_slots = models.PositiveSmallIntegerField(null=False, default=0)
    hdd_internal_slots = models.PositiveSmallIntegerField(null=False, default=1, choices=hdd_slots_choices)
    hdd_max_slots = models.PositiveSmallIntegerField(null=False, default=0)
    hdd_max_expansion_units_qty = models.PositiveSmallIntegerField(null=True)
    oneGb_nic_qty = models.PositiveSmallIntegerField(null=False, default=0, choices=oneGb_ports_qty_choices)
    tenGb_compatible = models.BooleanField(null=False, default=False)
    tenGb_nic_qty = models.PositiveSmallIntegerField(null=False, default=0)
    active = models.BooleanField(null=False, default=False)
    created_time = models.DateTimeField(auto_now_add=True,  null=False)
    updated_time = models.DateTimeField(auto_now=True, null=True)


    def __str__(self) -> str:
        return f'{self.maker.name} - {self.model}'

class Nas_Accessory(models.Model):
#    nas_model = models.ForeignKey(Nas_Model, on_delete=models.PROTECT, null=False, default=0)
    nas_model = models.ForeignKey(Nas_Model, on_delete=models.PROTECT)
    category = models.ForeignKey(Nas_Accessory_Category, on_delete= models.PROTECT)
    model = models.CharField(max_length=25, null=False, blank=False)
    msrp = models.FloatField(null=False)
    active = models.BooleanField(null=False, default=True)
    created_time = models.DateTimeField(auto_now_add=True, null=False)
    updated_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.nas_model.maker.name} {self.category.name} {self.model}'
