# Generated by Django 5.0.4 on 2024-06-09 14:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_equipmentonmission_equipment_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='allequipment',
            name='equipment_category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='allequipment',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='UserClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_mechanic', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]