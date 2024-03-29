# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-26 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_usluga'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paket_title', models.CharField(max_length=200, verbose_name='пакет')),
                ('paket_text', models.TextField(verbose_name='текст пакета')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуга',
            },
        ),
        migrations.AlterField(
            model_name='dom',
            name='dom',
            field=models.CharField(blank=True, max_length=200, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='usluga',
            name='usluga_text',
            field=models.TextField(verbose_name='текст услуги'),
        ),
    ]
