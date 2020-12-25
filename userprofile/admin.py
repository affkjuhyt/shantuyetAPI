from django.contrib import admin

# Register your models here.
from userprofile.models import UserProfile, Owner, SecondaryOwner


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'fullname', 'phone_number', 'email', 'gender', 'address',
                    'province']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = ['user']


admin.site.register(UserProfile , UserProfileAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'avatar', 'fullname', 'user_type', 'position', 'city', 'phone_number',
                    'current_status',
                    'date_modified', 'date_added']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = ['user']
    list_filter = ['current_status']


admin.site.register(Owner, OwnerAdmin)


class SecondaryOwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'fullname', 'phone_number', 'user_type', 'mission', 'current_status', 'date_modified',
                    'date_added']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = ['user']
    list_filter = ['current_status']


admin.site.register(SecondaryOwner, SecondaryOwnerAdmin)

