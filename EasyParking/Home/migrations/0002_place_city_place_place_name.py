# Generated by Django 4.1.2 on 2022-11-14 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='city',
            field=models.CharField(choices=[('Riyadh', 'Riyadh'), ('Jeddah', 'Jeddah'), ('Abha', 'Abha'), ('Makkah', 'Makkah'), ('Al-Medina', 'Al-Medina'), ('Al-Dammam', 'Al-Dammam')], default='Riyadh', max_length=64),
        ),
        migrations.AddField(
            model_name='place',
            name='place_name',
            field=models.CharField(default=None, max_length=2048),
            preserve_default=False,
        ),
    ]