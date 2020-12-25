from django.contrib import admin

# Register your models here.
from teas.models import Teas


class TeasAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'age', 'diameter', 'height',
                    'image1', 'image2', 'image3', 'image4')
    search_fields = ['name']
    raw_id_fields = ['owner']


admin.site.register(Teas, TeasAdmin)
