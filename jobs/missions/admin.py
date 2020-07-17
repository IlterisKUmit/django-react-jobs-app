from django.contrib import admin
from .models import Missions


# Register your models here.
class MissionsAdmin(admin.ModelAdmin):
    list_display = ('mission', 'is_completed', 'created_at')


admin.site.register(Missions, MissionsAdmin)
