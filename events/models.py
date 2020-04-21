from django.db import models

class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=120) 
    address = models.CharField(max_length=300)
    zip_code = models.CharField("Zip/Post Code", max_length=12)
    phone = models.CharField("Contact Phone", max_length=20)
    web = models.URLField("Web Address")
    email_address = models.EmailField("Email Address")
    
    def __str__(self):
        return self.name
    
class EventUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField("User Email")
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Event(models.Model):
    title = models.CharField("Event Name", help_text=u"Event Name", max_length=200)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, help_text=u"Event Location", blank=True, null=True, max_length=120)
    description = models.TextField("Event Description", help_text=u"Event Description and notes", blank=True, null=True)
    start_time = models.DateTimeField("Starting time", help_text=u"Event starting time and date")
    end_time = models.DateTimeField("End time", help_text=u"Event end time and date")
    attendees = models.ManyToManyField(EventUser)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"