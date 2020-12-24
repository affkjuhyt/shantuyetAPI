from django.contrib import admin

# Register your models here.
from userprofile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'fullname', 'phone_number', 'email', 'gender', 'address',
                    'province']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = ['user']


admin.site.register(UserProfile , UserProfileAdmin)

