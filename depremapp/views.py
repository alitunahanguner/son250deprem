from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize #fronttan gelen json datayı işler
from django.template.context import Context
import pandas as pd
from depremapp.boundeprem import vericek
from depremapp.models import SonDepremler
from django.contrib.gis.geos import Point

# Create your views here.


def tumdepremler_dataset(request):
    tumdepremler = serialize('geojson', SonDepremler.objects.all()[:250])
    return HttpResponse(tumdepremler, content_type='json')


def home(request):
    
    depremlerliste = vericek()
    sondepremler = []
    for i in depremlerliste:
        TarihveSaat = i[0]
        Enlem = float(i[1])
        Boylam = float(i[2])
        Derinlik = i[3]
        Buyukluk = i[4]
        Mekan = i[5]
        Sene = i[0][0:4]
        Ay = i[0][5:7]
        Gün = i[0][8:10]
        Saat = i[0][11:13]
        Dakika = i[0][14:16]
        liste = []
        tarihvesaat = TarihveSaat.replace(',','   ')
        liste.append(tarihvesaat)
        liste.append(i[5])
        liste.append(i[4])
        sondepremler.append(liste)

        try:
            SonDepremler(TarihveSaat=TarihveSaat,Derinlik=Derinlik,Buyukluk=Buyukluk,Mekan=Mekan,Sene=Sene,Ay=Ay,Gün=Gün,Saat=Saat,Dakika=Dakika,geom=Point(Boylam,Enlem)).save()
        except:
            pass
    """ Renders home page """
    sondepremler = sondepremler[:250]
    return render(request,'app/index.html',{"sondepremler":sondepremler})
