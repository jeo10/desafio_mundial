# Generated by Django 4.0.4 on 2022-11-16 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('codigo_seleccion', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Seleccion',
                'verbose_name_plural': 'Seleccionnes',
                'ordering': ['codigo_seleccion'],
            },
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('codigo_partido', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('horario', models.TimeField()),
                ('estadio', models.CharField(max_length=25)),
                ('fase', models.CharField(max_length=25)),
                ('equipo1', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='equipo1', to='mundial_predict.seleccion')),
                ('equipo2', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='equipo2', to='mundial_predict.seleccion')),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
            },
        ),
    ]
