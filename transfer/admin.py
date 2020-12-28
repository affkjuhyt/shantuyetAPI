from django.contrib import admin

# Register your models here.
from transfer.models import Transfer


class TransferAdmin(admin.ModelAdmin):
    list_display = ('id', 'tea', 'owner', 'secondary_owner', 'name', 'date', 'status')
    search_fields = ['name']
    raw_id_fields = ['tea', 'owner', 'secondary_owner']


admin.site.register(Transfer, TransferAdmin)
