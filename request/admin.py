from django.contrib import admin

# Register your models here.
from request.models import Request


class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'tea', 'owner', 'secondary_owner', 'name', 'date', 'request_status')
    search_fields = ['name']
    raw_id_fields = []


admin.site.register(Request, RequestAdmin)
