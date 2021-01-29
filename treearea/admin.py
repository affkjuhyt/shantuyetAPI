from django.contrib import admin
from treearea.models import TreeArea, Coordinate


class TreeAreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'acreage', 'number_tea', 'content']
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(TreeArea, TreeAreaAdmin)


class CoordinateAdmin(admin.ModelAdmin):
    list_display = ['id', 'lat', 'lon', 'tree_area']
    search_fields = ['tree_area']
    list_filter = ['tree_area']


admin.site.register(Coordinate, CoordinateAdmin)
