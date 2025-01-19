from django.contrib import admin
from .models import EventRegistration


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'interest_level', 'feedback')
    search_fields = ('name', 'email')  
    list_filter = ('interest_level',) 
    ordering = ('-id',) 

