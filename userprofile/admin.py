from django.contrib import admin

from userprofile.models import UserProfile, Owner, SecondaryOwner, Government


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'fullname', 'phone_number', 'email', 'address']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = ['user']


admin.site.register(UserProfile, UserProfileAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'fullname', 'phone_number', 'email', 'address']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = ['user']


admin.site.register(Owner, OwnerAdmin)


class SecondaryOwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'fullname', 'phone_number', 'email', 'address']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = ['user']


admin.site.register(SecondaryOwner, SecondaryOwnerAdmin)


class GovernmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'fullname', 'phone_number', 'email', 'address']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = ['user']


admin.site.register(Government, GovernmentAdmin)

