# Generated by Django 3.1.4 on 2022-11-08 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0010_auto_20221106_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço'),
        ),
    ]
