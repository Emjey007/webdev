from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserClassification, AllEquipment

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class User:
            model = UserClassification
            fields = ['job',
                      'username',
                      'first_name', 
                      'last_name', 
                      'email',
                      'password1', 
                      'password2']

class EquipmentForm(forms.ModelForm):
    equipment_id = forms.CharField(required=True)
    equipment_model = forms.CharField(required=True)
    equipment_category = forms.CharField(required=True)
    equipment_name = forms.CharField(required=True)
    equipment_description = forms.CharField(required=True)

    class Meta:
        model = AllEquipment
        fields = ['equipment_id', 
                  'equipment_model', 
                  'equipment_category',
                  'equipment_name', 
                  'equipment_description']
