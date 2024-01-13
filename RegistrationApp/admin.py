from django.contrib import admin
from RegistrationApp.models import Registration
from django import forms;
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=['Registrationdate','firstname', 'lastname','Email','rating'];

admin.site.register(Registration,RegistrationAdmin);