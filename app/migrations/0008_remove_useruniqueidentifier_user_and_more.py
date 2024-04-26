# Generated by Django 5.0 on 2024-03-09 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_useruniqueidentifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useruniqueidentifier',
            name='user',
        ),
        migrations.AddField(
            model_name='useruniqueidentifier',
            name='username',
            field=models.CharField(default='default_username', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='useruniqueidentifier',
            name='unique_identifier',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]
