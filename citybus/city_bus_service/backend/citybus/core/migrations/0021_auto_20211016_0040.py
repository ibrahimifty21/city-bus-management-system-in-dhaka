# Generated by Django 3.2.8 on 2021-10-15 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20211014_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeslot',
            options={'ordering': ['trip_number', 'time']},
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='bus_at_now',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_name', to='core.route'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='bus_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_name', to='core.bus'),
        ),
    ]