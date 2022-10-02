from django.urls.conf import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(
    r"multimedia",
    views.MediaViewSet,
)

urlpatterns = [
    path(
        "",
        include(router.urls),
    ),
]
