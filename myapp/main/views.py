from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import RegistrationForm, EquipmentForm
from .models import UserClassification, AllEquipment, EquipmentOnMission, EquipmentOnMaintenance, DamagedEquipment

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

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
    all_equipment = AllEquipment.objects.all()
    return render(request, 'all_equipment.html', {'all_equipment': all_equipment})

def equipment_on_mission(request):
    equipment_on_mission = EquipmentOnMission.objects.all()
    return render(request, 'equipment_on_mission.html', {'equipment_on_mission': equipment_on_mission})

def equipment_on_maintenance(request):
    equipment_on_maintenance = EquipmentOnMaintenance.objects.all()
    return render(request, 'equipment_on_maintenance.html', {'equipment_on_maintenance': equipment_on_maintenance})

def damaged_equipment(request):
    damaged_equipment = DamagedEquipment.objects.all()
    return render(request, 'damaged_equipment.html', {'damaged_equipment': damaged_equipment})

# Try
def deploy_equipment_on_mission(request, equipment_id):
    equipment = get_object_or_404(AllEquipment, id=equipment_id)
    EquipmentOnMission.objects.create(
        all_equipment=equipment,
        equipment_id_on_mission=equipment.equipment_id,
        equipment_model=equipment.equipment_model,
        equipment_category=equipment.equipment_category,
        equipment_name=equipment.equipment_name,
        equipment_description=equipment.equipment_description,
    )
    return redirect('all_equipment')

# HIRAP!
# def move_equipment_to_maintenance(request, equipment_id):
#     if request.method == 'POST':
#         equipment_form = EquipmentOnMaintenance(request.POST)
#         if equipment_form.is_valid():
#             equipment_form.save()
#             equipment = get_object_or_404(AllEquipment, id=equipment_id)
#         EquipmentOnMaintenance.objects.create(
#             all_equipment=equipment,
#             equipment_id_on_maintenance=equipment.equipment_id,
#             equipment_model=equipment.equipment_model,
#             equipment_category=equipment.equipment_category,
#             equipment_name=equipment.equipment_name,
#             equipment_description=equipment.equipment_description,
#         )
#     else:
#         equipment_form = EquipmentOnMaintenance()

#     return render(request, 'all_equipment.html', { 'equipment_form': equipment_form })

def move_equipment_to_maintenance(request, equipment_id):
    equipment = get_object_or_404(AllEquipment, id=equipment_id)
    EquipmentOnMaintenance.objects.create(
        all_equipment=equipment,
        equipment_id_on_maintenance=equipment.equipment_id,
        equipment_model=equipment.equipment_model,
        equipment_category=equipment.equipment_category,
        equipment_name=equipment.equipment_name,
        equipment_description=equipment.equipment_description,
    )
    return redirect('all_equipment')

def move_equipment_to_damaged_equipment(request, equipment_id):
    equipment = get_object_or_404(AllEquipment, id=equipment_id)
    DamagedEquipment.objects.create(
        all_equipment=equipment,
        equipment_id_on_damaged=equipment.equipment_id,
        equipment_model=equipment.equipment_model,
        equipment_category=equipment.equipment_category,
        equipment_name=equipment.equipment_name,
        equipment_description=equipment.equipment_description,
    )
    return redirect('all_equipment')

def remove_equipment_from_mission(request, equipment_id):
    equipment = get_object_or_404(AllEquipment, id=equipment_id)
    on_mission_equipment_instance = EquipmentOnMission.objects.filter(
        all_equipment=equipment,
        equipment_id_on_mission=equipment.equipment_id,
        equipment_model=equipment.equipment_model,
        equipment_category=equipment.equipment_category,
        equipment_name=equipment.equipment_name,
        equipment_description=equipment.equipment_description,
    ).first()

    if on_mission_equipment_instance:
        on_mission_equipment_instance.delete()
    
    return redirect('all_equipment')

def remove_equipment_from_maintenance(request, equipment_id):
    equipment = get_object_or_404(AllEquipment, id=equipment_id)
    on_maintenance_equipment_instance = EquipmentOnMaintenance.objects.filter(
        all_equipment=equipment,
        equipment_id_on_maintenance=equipment.equipment_id,
        equipment_model=equipment.equipment_model,
        equipment_category=equipment.equipment_category,
        equipment_name=equipment.equipment_name,
        equipment_description=equipment.equipment_description,
    ).first()

    if on_maintenance_equipment_instance:
        on_maintenance_equipment_instance.delete()
    
    return redirect('all_equipment')

# DI PA OKAY!
def from_mission_to_damaged_equipment(request, equipment_id):
    equipment = get_object_or_404(EquipmentOnMission, id=equipment_id)
    DamagedEquipment.objects.create(
        all_equipment=equipment,
        equipment_id_on_damaged=equipment.equipment_id_on_mission,
        equipment_model=equipment.equipment_model,
        equipment_category=equipment.equipment_category,
        equipment_name=equipment.equipment_name,
        equipment_description=equipment.equipment_description,
    )

    return redirect('all_equipment')

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
