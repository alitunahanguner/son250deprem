# Generated by Django 3.0.7 on 2020-06-16 16:15

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SonDepremler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TarihveSaat', models.CharField(max_length=100, unique=True)),
                ('Derinlik', models.CharField(max_length=100)),
                ('Buyukluk', models.CharField(max_length=100)),
                ('Mekan', models.CharField(max_length=100)),
                ('Sene', models.IntegerField()),
                ('Ay', models.IntegerField()),
                ('Gün', models.IntegerField()),
                ('Saat', models.IntegerField()),
                ('Dakika', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'SonDepremler',
            },
        ),
        migrations.CreateModel(
            name='WaterConsumption',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Suburb', models.CharField(max_length=100)),
                ('NoOfSingleResProp', models.IntegerField()),
                ('AvgMonthlyKL', models.IntegerField()),
                ('AvgMonthlyKLPredicted', models.IntegerField()),
                ('PredictionAccuracy', models.IntegerField()),
                ('Month', models.CharField(max_length=50)),
                ('Year', models.IntegerField()),
                ('DateTime', models.DateTimeField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'WaterConsumption',
            },
        ),
    ]
