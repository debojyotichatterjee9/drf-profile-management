from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "email",)


admin.site.register(UserProfile, UserProfileAdmin)
