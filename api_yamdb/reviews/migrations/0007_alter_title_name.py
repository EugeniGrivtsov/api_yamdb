# Generated by Django 3.2 on 2023-01-26 11:41

import reviews.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_title_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(
                max_length=256,
                validators=[reviews.validators.name_title_validator],
                verbose_name='Название произведения',
            ),
        ),
    ]
