from django import forms 
from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={"placeholder": "Your Name", "class": "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full", "style": "transition: all 0.15s ease 0s;"}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={"placeholder": "Your Email", "class": "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full", "style": "transition: all 0.15s ease 0s;"}))
    subject = forms.CharField(max_length=100, label="", required=False, widget=forms.TextInput(attrs={"placeholder": "Subject", "class": "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full", "style": "transition: all 0.15s ease 0s;"}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Type your Message ...", "rows": "4", "cols": "80", "class": "px-3 py-3 placeholder-gray-400 text-gray-700 bg-white rounded text-sm shadow focus:outline-none focus:shadow-outline w-full"}))
    
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
                cd.get("email", "francisc.furdui2@mail.dcu.ie"),
                ["francisc.furdui2@mail.dcu.ie"],
                connection=con
                )
            return HttpResponseRedirect("/contact?submitted=True")
    else:
        form = ContactForm()
        if "submitted" in request.GET:
            submitted = True
            
    return render(request, "contact.html", {"form": form, "submitted": submitted})