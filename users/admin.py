from django.contrib import admin
from .models import UserName

@admin.register(UserName)
class UserNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at',)
