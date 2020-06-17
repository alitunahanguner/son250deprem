from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from depremapp.boundeprem import vericek
from depremapp.models import SonDepremler
# Register your models here.

class SonDepremlerAdmin(LeafletGeoAdmin):
    pass


admin.site.register(SonDepremler, SonDepremlerAdmin)

