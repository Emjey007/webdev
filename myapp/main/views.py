from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegistrationForm, EquipmentForm
from .models import UserClassification, AllEquipment, EquipmentOnMission

# Create your views here.

def home_page(request):
    return HttpResponse("Hi!")

def account(request):
    accounts = UserClassification.objects.all()
    return render(request, 'account.html', {'accounts': accounts})

def signup(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect('home')
        else: 
            pass
    
    else: 
        user_form = RegistrationForm()

    return render(request, 'signup.html', {'user_form': user_form})

def client_signup(request):
    return render(request, 'client_signup.html')

def mechanic_signup(request):
    return render(request, 'mechanic_signup.html')

def add_equipment(request):
    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST)
        if equipment_form.is_valid():
            equipment_form.save()
            return redirect('home')
    else:
        equipment_form = EquipmentForm()

    return render(request, 'add_equipment.html', { 'equipment_form': equipment_form })

def all_equipment(request):
    equipments = AllEquipment.objects.filter

def available_equipment(request):
    available_equipments = AllEquipment.objects.filter(is_available=True)
    return render(request, 'available_equipment.html', {'available_equipments': available_equipments})

# def move_equipment(request):
#     if request.method == 'POST':
#         equipment_id = request.POST.get('equipment_id')
#         try:
#             equipment = AllEquipment.objects.get(id=equipment_id)
#             # Create an instance of EquipmentOnMission and save it
#             EquipmentOnMission.objects.create(
#                 equipment=equipment,
#                 equipment_model=equipment.equipment_model,
#                 equipment_name=equipment.equipment_name,
#                 equipment_description=equipment.equipment_description
#             )
#             return HttpResponse("Successfully moved equipment to EquipmentOnMission")
#         except AllEquipment.DoesNotExist:
#             return HttpResponse("Equipment does not exist")

#     equipment_list = AllEquipment.objects.all()
#     return render(request, 'move_equipment.html', {'equipment_list': equipment_list})

