from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("add_equipment/", views.add_equipment, name="add_equipment"),
]
