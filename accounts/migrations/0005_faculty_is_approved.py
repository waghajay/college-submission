# Generated by Django 5.1.7 on 2025-03-13 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
