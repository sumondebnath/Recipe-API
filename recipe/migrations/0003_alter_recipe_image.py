# Generated by Django 5.0.1 on 2024-05-22 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_alter_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/recipe/images/'),
        ),
    ]
