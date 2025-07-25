# Generated by Django 5.2.3 on 2025-07-01 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_rename_start_time_appointment_predicted_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='actual_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='predicted_duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('waiting', 'در انتظار'), ('in_progress', 'در حال درمان'), ('completed', 'تکمیل شده'), ('cancelled', 'لغو شده'), ('absent', 'عدم حضور')], default='waiting', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='treatment_type',
            field=models.CharField(max_length=100),
        ),
    ]
