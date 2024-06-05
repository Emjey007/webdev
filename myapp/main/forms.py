from django import forms
from .models import AllEquipment

class EquipmentForm(forms.ModelForm):
    equipment_id = forms.CharField(required=True)
    equipment_model = forms.CharField(required=True)
    equipment_name = forms.CharField(required=True)
    equipment_description = forms.CharField(required=True)

    class Meta:
        model = AllEquipment
        fields = ['equipment_id', 
                  'equipment_model', 
                  'equipment_name', 
                  'equipment_description']
        