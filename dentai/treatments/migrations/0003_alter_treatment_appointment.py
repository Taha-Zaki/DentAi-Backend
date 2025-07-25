# Generated by Django 5.2.3 on 2025-07-14 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_appointment_doctor_note'),
        ('treatments', '0002_treatment_delete_treatmentrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatment', to='appointments.appointment'),
        ),
    ]
