from django.contrib import admin
from .models import Incidences, Counties, Lp3
from leaflet.admin import LeafletGeoAdmin
# Register your models here.


class IncidencesAdmin(LeafletGeoAdmin):
	list_display =('name', 'location')


class CountiesAdmin(LeafletGeoAdmin):
	list_display =('counties', 'codes')


class Lp3Admin(LeafletGeoAdmin):
	list_display =('area', 'pkuid')


admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
admin.site.register(Lp3, Lp3Admin)


