""" Account's admin """
from django.contrib import admin

# Register your models here.
from assignment import models


@admin.register(models.Profile)
class UserAdmin(admin.ModelAdmin):
    """ User admin """
    list_display = ('id', 'user', 'bio', 'image',)
