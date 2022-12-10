# Generated by Django 2.2.5 on 2022-12-10 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_pedido_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='bairro',
            field=models.CharField(default='2022-02-20', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='cep',
            field=models.CharField(default='cep', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='cidade',
            field=models.CharField(default='cidade', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='complemento',
            field=models.CharField(default='complemento', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='numero',
            field=models.CharField(default='1', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='rua',
            field=models.CharField(default='rua', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=8, verbose_name='Total'),
            preserve_default=False,
        ),
    ]
