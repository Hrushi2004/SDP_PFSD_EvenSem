# Generated by Django 5.0 on 2024-03-09 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]