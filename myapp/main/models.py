from django.db import models

# Create your models here.

# This is the database for Client: ####

class AllEquipment(models.Model):
    equipment_id = models.CharField(max_length=100)
    equipment_model = models.CharField(max_length=100, unique=True) # This is our primary key to separate each
                                                                    # equipment with each other since they have
                                                                    # the same id to the same type of equipment.
    equipment_name = models.CharField(max_length=100)
    equipment_description = models.CharField(max_length=250)

    def __str__(self):
        return self.equipment_name

# class EquipmentOnMission(models.Model):
#     equipment_id = models.CharField(max_length=100)
#     equipment_model = models.CharField(max_length=100, unique=True)
#     equipment_name = models.CharField(max_length=100)

# class EquipmentNeedingRepair(models.Model):
#     equipment_id = models.CharField(max_length=100)
#     equipment_model = models.CharField(max_length=100, unique=True)
#     equipment_name = models.CharField(max_length=100)
#     equipment_issue_description = models.CharField(max_length=250)

# class BrokenEquipment(models.Model):
#     equipment_id = models.CharField(max_length=100)
#     equipment_model = models.CharField(max_length=100, unique=True)
#     equipment_name = models.CharField(max_length=100)

# class ReturnedEquipment(models.Model):
#     equipment_id = models.CharField(max_length=100)
#     equipment_model = models.CharField(max_length=100, unique=True)
#     equipment_name = models.CharField(max_length=100)
#     equipment_fixed_update = models.CharField(max_length=250)




# This is the database for Mechanics: ####

# class EquipmentToBeRepaired(models.Model): 
#     equipment_id = models.CharField(max_length=100)
#     equipment_model = models.CharField(max_length=100, unique=True)
#     equipment_name = models.CharField(max_length=100)
#     equipment_issue_description = models.CharField(max_length=250)

# class GiveBackEquipment(models.Model):
#     equipment_id = models.CharField(max_length=100)
#     equipment_model = models.CharField(max_length=100, unique=True)
#     equipment_name = models.CharField(max_length=100)
#     equipment_update = models.CharField(max_length=250)
