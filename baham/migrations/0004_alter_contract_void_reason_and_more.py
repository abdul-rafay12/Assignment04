# Generated by Django 4.2.1 on 2023-05-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baham', '0003_contract_created_by_contract_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='void_reason',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='void_reason',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='void_reason',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='void_reason',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
