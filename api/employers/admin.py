from django.contrib import admin
from .models import EmployerProfile, Job, Application

# Register your models here.
admin.site.register(EmployerProfile)
admin.site.register(Job)
admin.site.register(Application)
