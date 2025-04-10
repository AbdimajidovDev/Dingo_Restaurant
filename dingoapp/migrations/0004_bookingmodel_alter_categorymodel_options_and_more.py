# Generated by Django 5.0.6 on 2024-05-28 06:50

import dingoapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dingoapp', '0003_alter_cheflevel_ch_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222, verbose_name='Booking name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('num_of_g', models.IntegerField(default=0, verbose_name='Number of guests')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Phone number')),
                ('date', models.DateField(validators=[dingoapp.models.past_date_validator], verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('Note', models.TextField(blank=True, null=True, verbose_name='Your Note')),
            ],
        ),
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'ordering': ['created'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='chefmodel',
            options={'verbose_name': 'Chef', 'verbose_name_plural': 'Chefs'},
        ),
        migrations.AlterModelOptions(
            name='foodmodel',
            options={'verbose_name': 'Food', 'verbose_name_plural': 'Foods'},
        ),
    ]
