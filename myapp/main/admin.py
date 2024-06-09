from django.contrib import admin
from .models import UserClassification, AllEquipment, EquipmentOnMission

# Register your models here.
admin.site.register(UserClassification)
admin.site.register(AllEquipment)
admin.site.register(EquipmentOnMission)

