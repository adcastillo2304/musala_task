from django.contrib import admin

from .models import Medication, Drone, Shipping

# Register your models here.


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'model', 'weigth_limit',
                    'battery_capacity', 'state']
    list_filter = ['model', 'battery_capacity', 'state']
    ordering = ['serial_number']
    search_fields = ['serial_number']


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight', 'code', 'image']
    list_filter = ['name', 'weight', 'code']
    ordering = ['name', 'weight', 'code']
    search_fields = ['name', 'code']


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['drone']
