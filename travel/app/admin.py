from django.contrib import admin
from .models import Travel, Klass, Hotel

# Register your models here.


class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'term', 'klass', 'hotel')
    list_display_links = ('name',)


class KlassAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'price')
    list_display_links = ('type',)


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stars', 'price')
    list_display_links = ('name',)


admin.site.register(Travel)
admin.site.register(Klass)
admin.site.register(Hotel)