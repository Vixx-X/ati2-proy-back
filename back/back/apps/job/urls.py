from django.urls.conf import path, include
from . import views

job_urls = [
    path(
        "contract-modalities/",
        views.ContractModalityListView.as_view(),
        name="job-contract-modalities",
    ),
    path(
        "professions/",
        views.ProfessionListView.as_view(),
        name="job-professions",
    ),
]

urlpatterns = [
    path(
        "jobs/",
        include(job_urls),
    ),
]
