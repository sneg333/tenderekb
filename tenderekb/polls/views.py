from django.shortcuts import render, get_object_or_404, redirect
from .models import Dom, Usluga, Paket, Contact, Zakaz
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from .forms import ZakazCreateForm

def home(request):
    dom = Dom.objects.all()
    usluga = Usluga.objects.all()
    paket = Paket.objects.all()
    contact = Contact.objects.all()
    zakaz = Zakaz.objects.all()

    form = ZakazCreateForm()

    if request.method == "POST":
        form = ZakazCreateForm(request.POST)
        if form.is_valid():
            post = Zakaz()
            post.name = form.cleaned_data['name']
            post.email = form.cleaned_data['email']
            post.body_zakaz = form.cleaned_data['body_zakaz']
            post.save()
            return HttpResponseRedirect('/home')

    context = {
        'dom':dom,
        'usluga': usluga,
        'paket' : paket,
        'contact': contact,
        'zakaz': zakaz,
        'form': form,
    }

    return render(request,'polls/home.html', context)