# Generated by Django 5.0.1 on 2024-05-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]