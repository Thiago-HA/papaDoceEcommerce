# Generated by Django 3.1.4 on 2022-11-07 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_endereco_complemento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario_endereco',
            old_name='produto',
            new_name='endereco',
        ),
    ]
