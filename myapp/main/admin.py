from django.contrib import admin
from .models import UserClassification, AllEquipment, EquipmentOnMission, EquipmentOnMaintenance, DamagedEquipment, ReturnedEquipment

# Register your models here.
admin.site.register(UserClassification)
admin.site.register(AllEquipment)
admin.site.register(EquipmentOnMission)
admin.site.register(EquipmentOnMaintenance)
admin.site.register(DamagedEquipment)
admin.site.register(ReturnedEquipment)
