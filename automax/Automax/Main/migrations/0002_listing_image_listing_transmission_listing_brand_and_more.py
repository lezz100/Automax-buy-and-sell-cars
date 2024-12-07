# Generated by Django 5.1.1 on 2024-10-24 05:51

import Main.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
        ('Users', '0004_alter_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Image',
            field=models.ImageField(default='', upload_to=Main.utils.user_listing_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='Transmission',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='brand',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Nissan', 'Nissan'), ('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('BMW', 'BMW'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Audi', 'Audi'), ('Volkswagen', 'Volkswagen'), ('Hyundai', 'Hyundai'), ('Kia', 'Kia'), ('Mazda', 'Mazda'), ('Subaru', 'Subaru'), ('Jeep', 'Jeep'), ('Land Rover', 'Land Rover'), ('Jaguar', 'Jaguar'), ('Porsche', 'Porsche'), ('Tesla', 'Tesla'), ('Volvo', 'Volvo'), ('Lexus', 'Lexus')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='color',
            field=models.CharField(default='White', max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='engine',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.location'),
        ),
        migrations.AddField(
            model_name='listing',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='model',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='vin',
            field=models.CharField(default='', max_length=17),
            preserve_default=False,
        ),
    ]