# Generated by Django 5.0.4 on 2024-06-12 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_allequipment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allequipment',
            name='status',
        ),
    ]