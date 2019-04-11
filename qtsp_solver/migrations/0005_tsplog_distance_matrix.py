# Generated by Django 2.0.6 on 2018-07-23 10:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qtsp_solver', '0004_tsplog_distribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='tsplog',
            name='distance_matrix',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(null=True), null=True, size=None), null=True, size=None),
        ),
    ]