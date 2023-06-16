# Generated by Django 3.2.18 on 2023-04-10 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arboles_sembrados',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_siembra', models.DateField(verbose_name='%d-%m-%y')),
                ('cantidad', models.BigIntegerField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Coordenadas',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('longitud', models.BigIntegerField(max_length=255)),
                ('latitud', models.BigIntegerField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('nombre', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('nombre_cientifico', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nombre_común', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('nombre', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Departamento_nombre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appespecie.departamento')),
            ],
        ),
    ]
