# Generated by Django 2.2.5 on 2022-12-01 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0011_auto_20221108_2001'),
        ('pedido', '0002_auto_20221201_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido_Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.Pedido')),
                ('produto_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.Produto')),
            ],
        ),
    ]
