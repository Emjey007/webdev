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
    path("damaged_equipment/", views.damaged_equipment, name="damaged_equipment"),
    path("duplicate_equipment/<int:equipment_id>/", views.duplicate_equipment, name="duplicate_equipment"),
    path("duplicate_equipment1/<int:equipment_id>/", views.duplicate_equipment1, name="duplicate_equipment1"),
]
