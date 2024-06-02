from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EquipmentForm

# Create your views here.

def home_page(request):
    return HttpResponse("Hi!")

def add_equipment(request):
    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST)
        if equipment_form.is_valid():
            equipment_form.save()
            return redirect('home')
    else:
        equipment_form = EquipmentForm()

    return render(request, 'add_equipment.html', { 'equipment_form': equipment_form })

