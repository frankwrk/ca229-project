from django import forms 
from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100,label="Your Name")
    email = forms.EmailField(required=False,label="Your e-mail address")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg py-2 px-4 block w-full appearance-none leading-normal"
    
def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            con = get_connection("django.core.mail.backends.console.EmailBackend")
            send_mail(
                cd["subject"],
                cd["message"],
                cd.get("email", "noreply@example.com"),
                ['siteowner@example.com'],
                connection=con
                )
            return HttpResponseRedirect("/contact?submitted=True")
    else:
        form = ContactForm()
        if "submitted" in request.GET:
            submitted = True
            
    return render(request, "contact.html", {"form": form, "submitted": submitted})