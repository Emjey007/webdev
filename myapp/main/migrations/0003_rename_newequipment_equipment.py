# Generated by Django 5.0.4 on 2024-06-02 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_newequipment_equipment_date_added'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewEquipment',
            new_name='Equipment',
        ),
    ]
