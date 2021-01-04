from django.contrib import admin
from .models import User, ESPOut, ESPSensor

admin.site.register(User)
admin.site.register(ESPOut)
admin.site.register(ESPSensor)

# Register your models here.
