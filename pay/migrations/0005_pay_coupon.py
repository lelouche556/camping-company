# Generated by Django 2.2.1 on 2019-08-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0004_auto_20190810_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='coupon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]