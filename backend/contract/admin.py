from django.contrib import admin
from .models import Contract
from .models import Rates
# Register your models here.

admin.site.register(Contract)
admin.site.register(Rates)