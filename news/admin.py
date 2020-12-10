from django.contrib import admin

# Register your models here.
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_enable', 'is_hot', 'date_modified', 'date_added')
    search_fields = ['title']
    raw_id_fields = []
    list_filter = ['is_enable', 'is_hot']


admin.site.register(News, NewsAdmin)
