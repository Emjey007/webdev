from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.signup, name="login"),
    path("account/", views.account, name="account"),
    # path("client_signup/", views.client_signup, name="client_signup"),
    # path("mechanic_signup/", views.mechanic_signup, name="mechanic_signup"),
    path("add_equipment/", views.add_equipment, name="add_equipment"),
    path("available_equipment/", views.available_equipment, name="available_equipment"),
    # path("equipment_on_mission/", views.home_page, name="equipment_on_mission"),
    # path('move-equipment/', views.move_equipment, name='move_equipment'),
]
