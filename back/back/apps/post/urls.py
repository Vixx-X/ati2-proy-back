from django.urls.conf import path, include
from rest_framework import routers
from . import views
from back.apps.vehicle import views as vehicle
from back.apps.service import views as service
from back.apps.job import views as job

router = routers.DefaultRouter()
router.register(
    r"contact-seller",
    views.ContactSellerViewSet,
)
router.register(
    r"vehicle",
    vehicle.VehiclePostViewSet,
)
router.register(
    r"service",
    service.ServicePostViewSet,
)
router.register(
    r"job",
    job.JobPostViewSet,
)

day_options_urls = [
    path(
        "day-options/",
        views.DayOptionListView.as_view(),
        name="day-options",
    ),
]

urlpatterns = [
    path(
        "posts/",
        include(day_options_urls),
    ),
    path(
        "posts/",
        include(router.urls),
    ),
]
