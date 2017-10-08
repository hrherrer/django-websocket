from django.contrib import admin
from .models import *


class ScansInline(admin.TabularInline):
    model = Scan
    readonly_fields = ('create_date',)


class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'create_date')
    readonly_fields = ('create_date',)
    inlines = (ScansInline,)


admin.site.register(QRCode, QRCodeAdmin)
