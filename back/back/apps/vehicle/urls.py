from django.urls.conf import path, include
from . import views

vehicle_urls = [
    path(
        "brands/",
        views.BrandListView.as_view(),
        name="vehicle-brands",
    ),
    path(
        "models/",
        views.ModelListView.as_view(),
        name="vehicle-models",
    ),
    path(
        "years/",
        views.YearListView.as_view(),
        name="vehicle-years",
    ),
    path(
        "",
        views.VehicleListView.as_view(),
        name="vehicle-list",
    ),
    path(
        "",
        views.VehicleDetailView.as_view(),
        name="vehicle-detail",
    ),
]

urlpatterns = [
    path(
        "vehicles/",
        include(vehicle_urls),
    ),
]
