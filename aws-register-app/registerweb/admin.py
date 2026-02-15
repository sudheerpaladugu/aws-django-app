from django.contrib import admin

from . models import RegisterEmail, Person

admin.site.register(RegisterEmail)
admin.site.register(Person)