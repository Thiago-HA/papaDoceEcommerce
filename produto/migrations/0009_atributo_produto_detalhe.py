# Generated by Django 3.1.4 on 2022-11-04 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_auto_20221030_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atributo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto_detalhe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atributo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.atributo')),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]