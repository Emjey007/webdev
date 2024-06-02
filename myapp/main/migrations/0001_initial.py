# Generated by Django 5.0.4 on 2024-06-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_id', models.CharField(max_length=100)),
                ('equipment_model', models.CharField(max_length=100, unique=True)),
                ('equipment_name', models.CharField(max_length=100)),
                ('equipment_date_added', models.DateTimeField(auto_now_add=True)),
                ('equipment_description', models.CharField(max_length=250)),
            ],
        ),
    ]