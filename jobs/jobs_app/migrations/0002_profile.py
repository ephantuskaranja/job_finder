# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(choices=[('EMPLOYER', 'employer'), ('JOB_FINDER', 'job_finder')], max_length=60)),
            ],
        ),
    ]
