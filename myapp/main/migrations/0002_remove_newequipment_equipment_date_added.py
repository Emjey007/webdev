# Generated by Django 5.0.4 on 2024-06-02 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newequipment',
            name='equipment_date_added',
        ),
    ]
