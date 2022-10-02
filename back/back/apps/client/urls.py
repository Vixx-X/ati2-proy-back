from django.urls.conf import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r"natural-persons",
    views.NaturalPersonViewSet,
)

urlpatterns = [
    path(
        "natural-persons/register/",
        views.NaturalPersonRegistrationView.as_view(),
        name="natural-person-register",
    ),
    path(
        "",
        include(router.urls),
    ),
]
