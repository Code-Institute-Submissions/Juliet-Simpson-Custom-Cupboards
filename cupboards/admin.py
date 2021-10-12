from django.contrib import admin
from .models import Material, Cupboard, GalleryImage

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'material_id',
        'name',
        'price_per_m2',
    )

    ordering = ('display_name',)


class CupboardAdmin(admin.ModelAdmin):
    list_display = (
        'design_id',
        'name',
        'type',
        'material',
        'design_surcharge',
        'example_price',
        'main_image'
    )

    ordering = ('design_id',)


class GalleryImageAdmin(admin.ModelAdmin):
    list_display = (
        'cupboard',
        'file_name'
    )

    ordering = ('cupboard',)


admin.site.register(Material, MaterialAdmin)
admin.site.register(Cupboard, CupboardAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
