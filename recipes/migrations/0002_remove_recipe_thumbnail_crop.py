# Generated by Django 3.2.18 on 2023-05-12 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='thumbnail_crop',
        ),
    ]
