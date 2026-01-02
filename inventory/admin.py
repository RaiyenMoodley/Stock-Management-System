from django.contrib import admin
from .models import Radiator


@admin.register(Radiator)
class RadiatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'cost_price', 'selling_price', 'is_low_stock', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'compatible_vehicles']
    ordering = ['name']
    
    def is_low_stock(self, obj):
        return obj.is_low_stock()
    is_low_stock.boolean = True
    is_low_stock.short_description = 'Low Stock'
