from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Zakaz(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.EmailField()
    body_zakaz = models.CharField(max_length=400, verbose_name='текст')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Dom(models.Model):
    dom = models.CharField(max_length=200, verbose_name='заголовок', blank=True)
    onas_predtext = models.CharField(max_length=200, verbose_name='предтекст о нас', blank=True)
    onas_text = RichTextUploadingField(verbose_name='текст о нас')
    class Meta:
        verbose_name = 'дом'
        verbose_name_plural = 'дом'

    def __str__(self):
        return self.dom

class Usluga(models.Model):
    usluga = models.CharField(max_length=200, verbose_name='услуга')
    usluga_text = RichTextUploadingField( verbose_name='текст_услуги')
    image_usluga = models.ImageField(upload_to='post', blank=True)

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуга'

    def __str__(self):
        return self.usluga


class Podpaket(models.Model):
    podpaket_title = models.CharField(max_length=200, verbose_name='название подпакета')

    class Meta:
        verbose_name = 'подпакет'
        verbose_name_plural = 'подпакет'

    def __str__(self):
        return self.podpaket_title


class Paket(models.Model):
    paket_title = models.CharField(max_length=200, verbose_name='пакет')
    paket_text = RichTextUploadingField( verbose_name='текст_пакета')
    cena_paket = models.CharField(max_length=200, verbose_name='цена покета')
    podpaket_paket = models.ManyToManyField(Podpaket, verbose_name='покет')

    class Meta:
        verbose_name = 'пакет'
        verbose_name_plural = 'пакет'

    def __str__(self):
        return self.paket_title

class Contact(models.Model):
    contact_title = models.CharField(max_length=200, verbose_name='контакт')
    contact_text = RichTextUploadingField(verbose_name='текст_контакта', blank=True)
    email = models.CharField(max_length=200, verbose_name='email', blank=True)
    telefon = models.CharField(max_length=200, verbose_name='тел', blank=True)

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакт'

    def __str__(self):
        return self.contact_title