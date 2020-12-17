from django.contrib import admin

# Register your models here.
from userprofile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'phone_number', 'email', 'gender', 'address', 'dob', 'user_type',
                    'id_card', 'permanent_residence', 'issued_by', 'issued_date']
    search_fields = ['fullname', 'phone_number']
    raw_id_fields = []


admin.site.register(UserProfile , UserProfileAdmin)

