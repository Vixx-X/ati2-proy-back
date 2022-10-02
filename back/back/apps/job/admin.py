from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Profession, ContractModality

admin.site.register(ContractModality)
admin.site.register(Profession)
