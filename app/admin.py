from django.contrib import admin
from .models import *

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'count', 'last_updated')
    search_fields = ('page_name',)
    ordering = ('-last_updated',)
@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'ip_address', 'region', 'country', 'isp', 'accessed_at')
    list_filter = ('country', 'region', 'page_name')