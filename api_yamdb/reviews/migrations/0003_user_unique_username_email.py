# Generated by Django 3.2 on 2023-01-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20230119_1446'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(
                fields=('username', 'email'), name='unique_username_email'
            ),
        ),
    ]
