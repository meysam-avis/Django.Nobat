from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from erjaat.forms import ErjaatForm


def index(request):
    erjaat_form = ErjaatForm(request.POST)
    context = {
        'erjaat_form': erjaat_form
    }
    return render(request, 'erjaat/index.html', context)
