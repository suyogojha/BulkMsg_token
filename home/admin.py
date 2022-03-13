from django.contrib import admin

from home.models import message

# Register your models here.
@admin.register(message)
class messageAdmin(admin.ModelAdmin):
    list_display = ("name", "message", "contact", "email")
    list_filter = ("contact",)
    search_fields = ["name"]