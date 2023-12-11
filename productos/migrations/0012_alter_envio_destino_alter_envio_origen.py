# Generated by Django 4.2.7 on 2023-12-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_remove_electronicparts_parts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='destino',
            field=models.SmallIntegerField(choices=[(1, 'Ciudad de Mexico'), (2, 'Queretaro'), (3, 'Monterrey')]),
        ),
        migrations.AlterField(
            model_name='envio',
            name='origen',
            field=models.SmallIntegerField(choices=[(1, 'Toluca'), (2, 'Metepec')]),
        ),
    ]