# Generated by Django 3.2.4 on 2021-06-19 12:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='finished_after_deadline',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='finished_before_deadline',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
