# Generated by Django 2.0.7 on 2018-11-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_license_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='terms_condition',
            field=models.BooleanField(default=False),
        ),
    ]
