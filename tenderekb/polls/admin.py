from django.contrib import admin

from .models import Dom, Usluga, Paket, Podpaket, Contact, Zakaz

class ZakazAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email',
                    'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']

admin.site.register(Zakaz, ZakazAdmin)

admin.site.register(Dom)
admin.site.register(Usluga)
admin.site.register(Paket)
admin.site.register(Podpaket)
admin.site.register(Contact)