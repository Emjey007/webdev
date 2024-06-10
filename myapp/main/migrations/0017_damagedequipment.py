# Generated by Django 5.0.4 on 2024-06-10 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_allequipment_equipment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamagedEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_id_on_damaged', models.CharField(default='', max_length=100)),
                ('equipment_model', models.CharField(default='', max_length=100)),
                ('equipment_category', models.CharField(default='', max_length=100)),
                ('equipment_name', models.CharField(default='', max_length=100)),
                ('equipment_description', models.CharField(default='', max_length=250)),
                ('all_equipment1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.allequipment')),
            ],
        ),
    ]
