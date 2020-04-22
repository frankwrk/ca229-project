from datetime import date
import calendar
from calendar import HTMLCalendar
from django.shortcuts import render
from django.views.generic.base import TemplateView

def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "Events Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    return render(request, "calendar_base.html", {"title": title, "cal":cal})