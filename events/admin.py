from django.contrib import admin
from .models import Venue, EventUser, Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Create Events in the admin section."""
    ordering = ("-start_time",)
    search_fields = ["title", "venue", "start_time"]
    list_display = ("title", "venue", "start_time")
    list_filter = ("venue", "start_time")
    fieldsets = (
        ("Required Information", { 
            "description": "These fields are required for each event.",
            "fields": (("title", "venue"), "start_time")
        }),
        ("Optional Information", {
            "classes": ("collapse",),
            "fields": ("description", "manager")
        }),
    )
    
@admin.register(Venue) 
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone") 
    ordering = ("name",) 
    search_fields = ("name", "address")
    
@admin.register(EventUser) 
class EventUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email") 
    ordering = ("first_name",) 
    search_fields = ("name", "last_name")
