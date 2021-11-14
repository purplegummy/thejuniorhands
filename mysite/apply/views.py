from django.shortcuts import render, HttpResponseRedirect
from .forms import ApplicantForm
import smtplib
from email.message import EmailMessage
from django.contrib import messages

# Create your views here.


def apply(request, template="apply.html"):
    form = ApplicantForm()
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful! Make Sure To Check Your Email.')
            msg=EmailMessage()
            msg['Subject'] = 'Junior Hands Association Confirmation'
            msg['From'] = "Junior Hands Assocation"
            msg['To'] = form.cleaned_data['email']
            msg.set_content(" Test Email JHA " )
            
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("thejuniorhands@gmail.com", "handsbick2021")
            server.send_message(msg)
            server.quit() 
            
            return HttpResponseRedirect(request.path_info)
        
    print(form.errors.as_data())
    return render(request, template, {'form': form})

