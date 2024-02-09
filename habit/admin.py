from django.contrib import admin

from habit.models import Reflex


@admin.register(Reflex)
class ReflexAdmin(admin.ModelAdmin):
    list_display = ('id',)
