# Generated by Django 4.2.7 on 2023-12-07 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_inventario_delete_inventariopc_delete_inventariope_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario',
            name='BoM',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Activo'), (2, 'Desconectado'), (3, 'Ausente')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='stockl',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventario',
            name='stockr',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
