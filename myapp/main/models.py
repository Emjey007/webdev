from django.db import models

# Create your models here.

class Equipment(models.Model):
    equipment_id = models.CharField(max_length=100)
    equipment_model = models.CharField(max_length=100, unique=True)
    equipment_name = models.CharField(max_length=100)
    equipment_description = models.CharField(max_length=250)

    def __str__(self):
        return self.equipment_name
