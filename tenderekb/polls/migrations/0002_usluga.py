# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-26 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usluga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usluga', models.CharField(max_length=200, verbose_name='услуга')),
                ('usluga_text', models.TextField(max_length=200, verbose_name='текст')),
                ('image_usluga', models.ImageField(blank=True, upload_to='post')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуга',
            },
        ),
    ]