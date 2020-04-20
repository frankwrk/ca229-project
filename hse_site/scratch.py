import os
import sys

# needed for Sublime Text 3
# sys.path.append('PATHTOPROJECT/hse_site')
# set the Django settings module before initializing Django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "hse_site.settings"
)
import django

django.setup()
