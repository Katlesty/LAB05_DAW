# Generated by Django 5.0.4 on 2024-04-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
    ]
