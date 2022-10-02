from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import ContactSeller, DayOption

admin.site.register(DayOption)
admin.site.register(ContactSeller)
