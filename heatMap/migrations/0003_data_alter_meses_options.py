# Generated by Django 4.1.7 on 2023-03-18 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heatMap', '0002_alter_meses_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='heatMap.coordenadas')),
                ('valor', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='meses',
            options={'managed': False},
        ),
    ]
