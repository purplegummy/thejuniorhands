from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import template
from .models import Contact, upcomingEvent, Subscription
from .forms import ContactForm, EmailForm, VolunteerForm
import smtplib
from email.message import EmailMessage
from django.contrib import messages
# Create your views here.
register = template.Library()
def index(request, template="index.html"):
    events = upcomingEvent.objects.all()
    return render(request, template, {'events': events})

def donate(request, template="donate.html"):
    return render(request, template, {})
    
def base(request, template="base.html"):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted! Check your email for more information.')
            
            return HttpResponseRedirect(request.path_info)
        
    return render(request, template, {'form': form})

def about(request, template="about.html"):
    return render(request, template, {})

def contact(request, template="contact.html"):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            msg=EmailMessage()
            msg['Subject'] = form.cleaned_data['subject'] + " from " +form.cleaned_data['email']
            msg['From'] = "thejuniorhands@gmail.com"
            msg['To'] = "thejuniorhands@gmail.com"
            msg.set_content(form.cleaned_data['message'])
            
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("thejuniorhands@gmail.com", "handsbick2021")
            server.send_message(msg)
            server.quit() 
            
            return HttpResponseRedirect(request.path_info)
        
    
    return render(request, template, {'form': form})

def event(request, template="events.html"):
    events = upcomingEvent.objects.all()
    return render(request, template,  {'events': events} )

def volunteer(request, template="volunteer.html"):
    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Volunteer Request Has Been Submitted.')
            return HttpResponseRedirect(request.path_info)
    return render(request, template, {"form": form})

@register.simple_tag
def get_index(obj, item):

    return obj.index(item)
       
