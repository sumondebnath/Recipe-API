# Generated by Django 5.0.1 on 2024-05-20 19:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_useraccount_bio_alter_useraccount_password'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='email',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='password',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='username',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]