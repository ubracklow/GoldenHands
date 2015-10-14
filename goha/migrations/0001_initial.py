# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField()),
                ('location', models.CharField(max_length=250)),
                ('number_of_guests', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('guest_name', models.CharField(max_length=50)),
                ('guest_email', models.EmailField(max_length=254)),
                ('guest_task', models.CharField(blank=True, max_length=50)),
                ('related_event', models.ForeignKey(to='goha.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('host_name', models.CharField(max_length=50)),
                ('host_email', models.EmailField(max_length=254)),
                ('host_choice', models.CharField(choices=[('SA', 'Salty'), ('SW', 'Sweet'), ('DR', 'Drink'), ('IDC', 'I dont care')], max_length=3)),
                ('related_event', models.ForeignKey(to='goha.Event')),
            ],
        ),
    ]
