from django.urls.conf import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r"businesses",
    views.BusinessViewSet,
)

urlpatterns = [
    path(
        "businesses/register/",
        views.BusinessRegistrationView.as_view(),
        name="business-register",
    ),
    path(
        "",
        include(router.urls),
    ),
]
