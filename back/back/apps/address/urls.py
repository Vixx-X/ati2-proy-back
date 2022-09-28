from django.urls.conf import path, include
from . import views

address_urls = [
    path(
        "continents/",
        views.ContinentListView.as_view(),
        name="address-continents",
    ),
    path(
        "countries/",
        views.CountryListView.as_view(),
        name="address-countries",
    ),
    path(
        "states/",
        views.StateListView.as_view(),
        name="address-states",
    ),
    path(
        "cities/",
        views.CityListView.as_view(),
        name="address-cities",
    ),
]

urlpatterns = [
    path(
        "addresses/",
        include(address_urls),
    ),
]
