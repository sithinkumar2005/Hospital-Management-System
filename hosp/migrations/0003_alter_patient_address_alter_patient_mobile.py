# Generated by Django 5.0.6 on 2024-05-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp', '0002_rename_appoinment_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]
