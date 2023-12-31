# Generated by Django 4.2.1 on 2023-06-15 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=30)),
                ('precio_producto', models.CharField(max_length=30)),
                ('cantidad_producto', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='imagenesProducto')),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.categoria')),
            ],
        ),
    ]
