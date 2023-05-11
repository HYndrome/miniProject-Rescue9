# Generated by Django 3.2.18 on 2023-05-11 05:29

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('recipes', '0004_alter_recipe_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='used_products',
            field=models.ManyToManyField(blank=True, related_name='used_recipes', to='products.Product'),
        ),
    ]