# Generated by Django 2.0.7 on 2019-05-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_vehicledefinition_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledefinition',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
