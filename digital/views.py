from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties, Incidences, Lp3


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


def County_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')


def Incidence_data(request):
    points = serialize('geojson', Incidences.objects.all())
    return HttpResponse(points, content_type='json')


def Lp3_parcels(request):
    parcels = serialize('geojson', Lp3.objects.all())
    return HttpResponse(parcels, content_type='json')


