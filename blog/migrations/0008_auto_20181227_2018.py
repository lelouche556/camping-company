# Generated by Django 2.0.7 on 2018-12-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='blog_image2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='blog_image'),
        ),
    ]
