# Generated by Django 4.1.4 on 2023-01-10 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='directores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=100)),
                ('edad', models.IntegerField()),
                ('nacionalidad', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=50)),
                ('anio', models.IntegerField()),
                ('genero', models.TextField(max_length=50)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directores.directores')),
            ],
        ),
        migrations.CreateModel(
            name='sinopsis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sinopsis', models.TextField(max_length=500)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directores.peliculas')),
            ],
        ),
    ]
