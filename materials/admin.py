from django.contrib import admin
from materials.models import Material


@admin.register(Material)
class AdminMaterial(admin.ModelAdmin):
    list_display = ("pk", "title", "content", "is_published" )
