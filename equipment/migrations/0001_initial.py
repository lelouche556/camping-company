# Generated by Django 2.0.7 on 2018-10-02 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yellow_box', models.BooleanField()),
                ('kettel', models.BooleanField()),
                ('utensils', models.BooleanField()),
                ('stove', models.BooleanField()),
                ('bbq_grill', models.BooleanField()),
                ('spare_tyre', models.BooleanField()),
                ('shovel', models.BooleanField()),
                ('mug_bucket', models.BooleanField()),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_check', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
