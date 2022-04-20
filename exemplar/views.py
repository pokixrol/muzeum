from django.shortcuts import render
from exemplar.models import Exemplar, Odvetvi, Priloha


def index(request):
    pocet_exemplaru = Exemplar.objects.all().count()

    exemplre = Exemplar.objects.order_by('-datum_vytvoreni')[:3]

    context = {
        'pocet_exemplaru': pocet_exemplaru,
        'exemplare': exemplre
    }

    return render(request, 'index.html', context=context)
