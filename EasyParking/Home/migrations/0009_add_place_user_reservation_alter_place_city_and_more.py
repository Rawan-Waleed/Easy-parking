# Generated by Django 4.1.3 on 2022-11-16 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0008_alter_add_place_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=2048, null=True)),
                ('address', models.URLField(default='https://www.google.com/maps/')),
                ('Price', models.CharField(max_length=2048)),
                ('number_parking', models.IntegerField()),
                ('days', models.CharField(max_length=64)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Add',
        ),
    ]
