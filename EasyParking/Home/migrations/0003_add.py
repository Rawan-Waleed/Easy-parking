# Generated by Django 4.1.3 on 2022-11-15 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0002_place_city_place_place_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('Price', models.CharField(max_length=2048)),
                ('number_parking', models.IntegerField()),
                ('days', models.CharField(choices=[('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Al-Wednesday', 'Al-Wednesday'), ('Al-Thursday', 'Al-Thursday'), ('Friday', 'Friday')], default='Saturday', max_length=64)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
