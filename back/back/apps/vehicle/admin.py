from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Vehicle

admin.site.register(Vehicle)
