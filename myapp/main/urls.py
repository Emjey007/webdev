from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.signup, name="login"),
    path("account/", views.account, name="account"),
    path("add_equipment/", views.add_equipment, name="add_equipment"),
    path("all_equipment/", views.all_equipment, name="all_equipment"),
    path("equipment_on_mission/", views.equipment_on_mission, name="equipment_on_mission"),
    path("equipment_on_maintenance/", views.equipment_on_maintenance, name="equipment_on_maintenance"),
    path("damaged_equipment/", views.damaged_equipment, name="damaged_equipment"),
    path("deploy_equipment_on_mission/<int:equipment_id>/", views.deploy_equipment_on_mission, name="deploy_equipment_on_mission"),
    path("move_equipment_to_maintenance/<int:equipment_id>/", views.move_equipment_to_maintenance, name="move_equipment_to_maintenance"),
    path("move_equipment_to_damaged_equipment/<int:equipment_id>/", views.move_equipment_to_damaged_equipment, name="move_equipment_to_damaged_equipment"),
    path("remove_equipment_from_mission/<int:equipment_id>/", views.remove_equipment_from_mission, name="remove_equipment_from_mission"),
    path("remove_equipment_from_maintenance/<int:equipment_id>/", views.remove_equipment_from_maintenance, name="remove_equipment_from_maintenance"),
    # Mga di ko pa magawa:
    path("from_mission_to_damaged_equipment/<int:equipment_id>/", views.from_mission_to_damaged_equipment, name="from_mission_to_damaged_equipment"),
]
