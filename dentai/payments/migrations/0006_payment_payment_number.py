# Generated by Django 5.2.3 on 2025-07-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_payment_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
