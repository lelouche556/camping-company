# Generated by Django 2.0.7 on 2019-05-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20190503_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lead_status',
            field=models.CharField(blank=True, choices=[('Lead Closed', 'Lead Closed'), ('Follow Up', 'Follow Up')], default='Follow Up', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='license_number',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nickname',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
