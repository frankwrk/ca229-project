from django.contrib import admin
from .models import Event

admin.site.register(Event)

class EventAdmin(admin.ModelAdmin):
    """Create Events in the admin section."""
    date_hierarchy = "created"
    search_fields = ["title", "venue", "start_time"]
    list_display = ("title", "venue", "description", "user" "start_time", "end_time")
    list_filter = ("status",)
