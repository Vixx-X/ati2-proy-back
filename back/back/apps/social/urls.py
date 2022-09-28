from django.urls.conf import path
from . import views

urlpatterns = [
    path(
        "socials/",
        views.SocialListView.as_view(),
        name="socials",
    ),
]
