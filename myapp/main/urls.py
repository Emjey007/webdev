from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("add_equipment/", views.add_equipment, name="add_equipment"),
    path("available_equipment/", views.available_equipment, name="available_equipment"),
]
