from django.contrib import admin
from . import models

# Register your models here.
class SpecializationAdminModel(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}

class DesignationModelAdmin(admin.ModelAdmin):
        prepopulated_fields={"slug":("name",)}



admin.site.register(models.Designation,DesignationModelAdmin)
admin.site.register(models.Specialization,SpecializationAdminModel)
admin.site.register(models.AvailableTime)
admin.site.register(models.Doctor)


