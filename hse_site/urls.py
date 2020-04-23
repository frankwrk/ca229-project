from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import contact

admin.site.site_header = "Events Project Dashboard"
admin.site.site_title = "Admin"
admin.site.site_url = "/"
admin.site.index_title = "Activity Events Locations Dashboard"
admin.empty_value_display = "**Empty**"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/password_reset/", auth_views.PasswordResetView.as_view(), name="admin_password_reset", ),
    path("admin/password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done", ),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm", ),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete", ),
    path("", TemplateView.as_view(template_name="base.html")),
    path("calendar/", include("events.urls")),
    path("contact/", contact.contact, name="contact"),
]
