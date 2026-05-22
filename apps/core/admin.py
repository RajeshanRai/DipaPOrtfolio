from django.contrib import admin
from .models import CVDownload


@admin.register(CVDownload)
class CVDownloadAdmin(admin.ModelAdmin):
    list_display = ('created', 'ip', 'user_agent')
    readonly_fields = ('created', 'ip', 'user_agent')
    ordering = ('-created',)
