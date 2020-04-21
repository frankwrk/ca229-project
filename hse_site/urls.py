from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="base.html")),
    path("calendar/", TemplateView.as_view(template_name="calendar.html")),
    path("contact/", TemplateView.as_view(template_name="contact.html")),
]
