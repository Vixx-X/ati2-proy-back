from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import ContactSeller, DayOption

from back.apps.vehicle.models import VehiclePost
from back.apps.job.models import JobPost
from back.apps.service.models import ServicePost

admin.site.register(DayOption)
admin.site.register(ContactSeller)

admin.site.register(VehiclePost)
admin.site.register(JobPost)
admin.site.register(ServicePost)
