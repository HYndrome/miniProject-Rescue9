# Generated by Django 3.2.18 on 2023-05-17 05:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields
import imagekit.models.fields
import recipes.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('thumbnail_upload', models.ImageField(upload_to=recipes.models.recipe_thumbnail_path)),
                ('thumbnail_crop', models.ImageField(upload_to='thumbnail_crop')),
                ('category', models.CharField(max_length=20)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_users', models.ManyToManyField(related_name='like_recipes', to=settings.AUTH_USER_MODEL)),
                ('used_products', models.ManyToManyField(blank=True, related_name='used_recipes', to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=recipes.models.review_img_path)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('like_user', models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
