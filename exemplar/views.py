from django.shortcuts import render
from exemplar.models import Exemplar, Odvetvi, Priloha
from django.views.generic import ListView


def index(request):
    pocet_exemplaru = Exemplar.objects.all().count()

    exemplre = Exemplar.objects.order_by('nazev')[:3]

    context = {
        'pocet_exemplaru': pocet_exemplaru,
        'exemplare': exemplre
    }

    return render(request, 'index.html', context=context)


class ExemplarListView(ListView):
    model = Exemplar

    context_object_name = 'list_exemplaru'

    template_name = 'list.html'


def easteregg(request):

    return render(request, 'eatreregg/index.html')