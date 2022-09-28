from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models

admin.site.register(models.Continent)
admin.site.register(models.Country)
admin.site.register(models.State)
admin.site.register(models.City)
admin.site.register(models.Address)
