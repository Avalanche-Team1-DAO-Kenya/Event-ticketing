from django.contrib import admin
from .models import EventRegistration


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'name', 'email', 'phone_number' , 'interest_level' , 'feedback') 
    list_filter = ('timestamp',) 
    search_fields = ('name', 'email') 


admin.site.register(EventRegistration, EventRegistrationAdmin)
