# Generated by Django 3.0.3 on 2020-04-27 23:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('ticker', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('vpa', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('pvp', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('day', models.DateField()),
            ],
            options={
                'ordering': ['ticker'],
            },
        ),
    ]
