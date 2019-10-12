from django.contrib import admin

# Register your models here.

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date','is_mvp')
    list_editable = ('is_mvp',)

admin.site.register(Realtor, RealtorAdmin)
