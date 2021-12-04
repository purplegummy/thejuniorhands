from django.contrib import admin
from .models import upcomingEvent, Contact, Volunteer
# Register your models here.

admin.site.register(upcomingEvent)
admin.site.register(Contact)
admin.site.register(Volunteer)