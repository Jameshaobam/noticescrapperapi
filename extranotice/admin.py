from django.contrib import admin
from .models import ExtraNotice

class ExtraNoticeAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'date')

admin.site.register(ExtraNotice,ExtraNoticeAdmin)
