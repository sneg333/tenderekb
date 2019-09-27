# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-27 11:14
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254)),
                ('body_zakaz', models.CharField(max_length=400, verbose_name='текст')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='текст_контакта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telefon',
            field=models.CharField(blank=True, max_length=200, verbose_name='тел'),
        ),
    ]