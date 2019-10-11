from django.contrib import admin
from .models import Sale


# Register your models here.
class SalesAdmin(admin.ModelAdmin):
    search_fields = ('id', 'customer_id',)
    list_display = (
        'id', 'dop', 'customer_id', 'fuel', 'vehicle_segment', 'selling_price', 'power_steering', 'airbags', 'sunroof',
        'matt_finish', 'music_system', 'customer_gender', 'customer_income_group', 'customer_region',
        'customer_marital_status')
    list_display_links = ()

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['dop']
        return []

admin.site.register(Sale, SalesAdmin)
