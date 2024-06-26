# Generated by Django 5.0 on 2024-03-09 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_blog_author_blog_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUniqueIdentifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_identifier', models.CharField(max_length=100, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
        ),
    ]
