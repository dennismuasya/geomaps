from django.conf.urls import include, url
from .views import HomePageView, County_datasets, Incidence_data, Lp3_parcels

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^county_data/$', County_datasets, name='county'),
    url(r'^incidence_data/$', Incidence_data, name='incidences'),
    url(r'^lp3_data/$', Lp3_parcels, name='lp3'),

]