# Generated by Django 2.2.1 on 2019-09-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0013_circuit'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuit',
            name='para21',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='circuit',
            name='para22',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='circuit',
            name='para23',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuit',
            name='para31',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='circuit',
            name='para32',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='circuit',
            name='para33',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuit',
            name='para41',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='circuit',
            name='para42',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='circuit',
            name='para43',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circuit',
            name='para51',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='circuit',
            name='para52',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='circuit',
            name='para53',
            field=models.TextField(default='b'),
            preserve_default=False,
        ),
    ]
