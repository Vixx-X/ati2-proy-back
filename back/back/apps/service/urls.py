from django.urls.conf import path
from . import views

urlpatterns = [
    path(
        "services/",
        views.ServiceListView.as_view(),
        name="services",
    ),
]
