# Generated by Django 3.1.4 on 2022-11-06 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20221106_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
