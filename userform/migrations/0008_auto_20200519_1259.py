# Generated by Django 3.0.5 on 2020-05-19 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0007_auto_20200519_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails1',
            name='hotel1',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userform.Hotelinfo'),
        ),
        migrations.AlterField(
            model_name='bookingdetails1',
            name='room1',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userform.Roominformation'),
        ),
    ]
