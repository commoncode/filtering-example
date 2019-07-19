from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, UserChangeForm

from . import models


class DoctorUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = models.Doctor


class DoctorUserAdmin(UserAdmin):
    form = DoctorUserChangeForm

    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("practice",)}),)


admin.site.register(models.Doctor, DoctorUserAdmin)
admin.site.register(models.Practice)
admin.site.register(models.Patient)
admin.site.register(models.Appointment)
