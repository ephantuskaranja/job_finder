# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 07:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('skill', models.CharField(choices=[('PYTHON', 'python'), ('CSHARP', 'c#'), ('JAVA', 'java'), ('C', 'c'), ('RUBY', 'ruby')], max_length=60)),
                ('location', models.CharField(choices=[('MAYOR_ROAD', 'mayor_road'), ('RONGAI', 'rongai'), ('GATAKA', 'gataka'), ('OLOLUA', 'ololua')], max_length=60)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('job_type', models.CharField(choices=[('PERMANENT', 'permanent'), ('CONTRACT', 'contract'), ('PART_TIME', 'part_time')], max_length=60)),
                ('contact', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
