from django.urls.conf import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(
    r"contact-me",
    views.ContactMeViewSet,
)

urlpatterns = [
    path(
        "about/",
        include(router.urls),
    ),
]
