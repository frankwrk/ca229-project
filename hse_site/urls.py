from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

admin.site.site_header = "HSE Project Dashboard"
admin.site.site_title = "Admin"
admin.site.site_url = "/"
admin.site.index_title = "HSE Locations Dashboard"
admin.empty_value_display = "**Empty**"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="base.html")),
    path("calendar/", include("events.urls")),
    path("page/", include("pages.urls")),
    path("contact/", TemplateView.as_view(template_name="contact.html")),
    
]
