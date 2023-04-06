from django.contrib import admin
from .models import EmployerProfile, Job

# Register your models here.
admin.site.register(EmployerProfile)
admin.site.register(Job)
