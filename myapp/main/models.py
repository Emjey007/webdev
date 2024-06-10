from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This is the database for Client: ####

class UserClassification(models.Model):
    # is_mechanic = models.BooleanField(default=False)
    # is_client = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    job = models.IntegerField(choices=[(1, 'User'), (2, 'Mechanic')], null=True, blank=True)

    def __str__(self):
        return self.user.username

class AllEquipment(models.Model):
    equipment_id = models.CharField(max_length=100, default='', blank=False)
    equipment_model = models.CharField(max_length=100, unique=True) 
    equipment_category = models.CharField(max_length=100, default='', blank=False) 
    equipment_name = models.CharField(max_length=100, default='', blank=False)
    equipment_description = models.CharField(max_length=250, default='', blank=False)

    def __str__(self):
        return self.equipment_name
    
class EquipmentOnMission(models.Model):
    all_equipment = models.ForeignKey(AllEquipment, on_delete=models.CASCADE)
    equipment_id_on_mission = models.CharField(max_length=100, default='', blank=False)
    equipment_model = models.CharField(max_length=100, default='', blank=False)
    equipment_category = models.CharField(max_length=100, default='', blank=False)
    equipment_name = models.CharField(max_length=100, default='', blank=False)
    equipment_description = models.CharField(max_length=250, default='', blank=False)

    def __str__(self):
        return self.equipment_model

class DamagedEquipment(models.Model):
    all_equipment = models.ForeignKey(AllEquipment, on_delete=models.CASCADE)
    equipment_id_on_damaged = models.CharField(max_length=100, default='', blank=False)
    equipment_model = models.CharField(max_length=100, default='', blank=False)
    equipment_category = models.CharField(max_length=100, default='', blank=False)
    equipment_name = models.CharField(max_length=100, default='', blank=False)
    equipment_description = models.CharField(max_length=250, default='', blank=False)

    def __str__(self):
        return self.equipment_model
    