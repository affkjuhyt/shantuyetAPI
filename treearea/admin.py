from django.contrib import admin
from treearea.models import TreeArea


class TreeAreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'acreage', 'number_tea', 'content']
    search_fields = ['name']


admin.site.register(TreeArea, TreeAreaAdmin)
