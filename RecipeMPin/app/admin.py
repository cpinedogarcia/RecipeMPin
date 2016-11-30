from app.models import TwoStep
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class TwoStepInline(admin.StackedInline):
    model = TwoStep
    can_delete = False
    verbose_name_plural = 'pin'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (TwoStepInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
