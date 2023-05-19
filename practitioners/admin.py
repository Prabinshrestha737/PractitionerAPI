from django.contrib import admin
from .models import Practitioner, Qualification, Communication


admin.site.register(Practitioner)
admin.site.register(Qualification)
admin.site.register(Communication)
