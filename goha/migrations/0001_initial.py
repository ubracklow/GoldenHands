# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('guest_name', models.CharField(max_length=50)),
                ('guest_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MyEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('host_name', models.CharField(max_length=50)),
                ('host_email', models.EmailField(max_length=254)),
                ('date_time', models.DateTimeField()),
                ('location', models.CharField(max_length=250)),
                ('number_of_guests', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='related_event',
            field=models.ForeignKey(to='goha.MyEvent'),
        ),
    ]
