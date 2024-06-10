from django.contrib import admin
from .models import UserClassification, AllEquipment, EquipmentOnMission, DamagedEquipment

# Register your models here.
admin.site.register(UserClassification)
admin.site.register(AllEquipment)
admin.site.register(EquipmentOnMission)
admin.site.register(DamagedEquipment)
