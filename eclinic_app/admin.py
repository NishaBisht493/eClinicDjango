from django.contrib import admin

# Register your models here.
from .models import Appointment, Contact, Comment, Doctor
admin.site.register(Appointment)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Doctor)