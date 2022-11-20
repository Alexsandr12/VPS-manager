from django.contrib import admin

from .models import Vps


class VpsAdmin(admin.ModelAdmin):
    list_display = ("uid", "cpu", "hdd", "ram", "status")
    fields = ("cpu", "hdd", "ram", "status")


admin.site.register(Vps, VpsAdmin)
