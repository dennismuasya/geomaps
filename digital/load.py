import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties, Lp3


# Auto-generated `LayerMapping` dictionary for Counties model
counties_mapping = {
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'counties.shp'),
)


# def run(verbose=True):
#     lm = LayerMapping(Counties, county_shp, counties_mapping, transform=False, encoding='iso-8859-1')
#     lm.save(strict=True, verbose=verbose)

Lp3_mapping = {
    'pkuid': 'pkuid',
    'area': 'AREA',
    'geom': 'MULTIPOLYGON',
}

LP3_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'LP3.shp'),
)


def run(verbose=True):
    lm = LayerMapping(Lp3, LP3_shp, Lp3_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)