# Generated by Django 4.1.3 on 2022-11-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_add_place_user_reservation_alter_place_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reservation',
            name='day',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user_reservation',
            name='hours',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user_reservation',
            name='parking_reserve',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='user_reservation',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
