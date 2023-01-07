# Generated by Django 4.1.4 on 2023-01-06 05:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('HIFU Face', 'HIFU Face'), ('HIFU Body', 'HIFU Body'), ('HIFU Vagin', 'HIFU Vagin')], default='HIFU Face', max_length=50)),
                ('day', models.DateField(default=datetime.datetime(2023, 1, 6, 5, 19, 21, 932008))),
                ('time', models.CharField(choices=[('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'), ('12:00 PM', '12:00 PM'), ('1:00 PM', '1:00 PM'), ('3:00 PM', '3:00 PM'), ('4:00 PM', '4:00 PM'), ('5:00 PM', '5:00 PM'), ('6:00 PM', '6:00 PM')], default='10:00 AM', max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
