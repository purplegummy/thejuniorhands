from django.db import models

class upcomingEvent(models.Model):
    eventName = models.CharField(max_length=200)
    day = models.CharField(max_length=15)
    month = models.CharField(max_length=3)
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=40)
    desc = models.CharField(max_length=700)
    def __str__(self):
            return self.eventName + " " + self.month.lower().capitalize()+ " " + self.day


class Contact(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=600)

    def __str__(self):
        return self.firstName + " " + self.lastName + " " + self.subject

class Subscription(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Volunteer(models.Model):
    objs = upcomingEvent.objects.all()
    names = objs.values('eventName')
    days = objs.values('day')
    months = objs.values('month')
    times = objs.values('time')
    choices = []
    for i in range(len(names)):
        choice = ((names[i]['eventName'], names[i]['eventName'] + " @" + months[i]['month'].upper() + " " + days[i]['day'] +  " : " + times[i]['time']))
        choices.append(choice)
    print(choices)
    event = models.CharField(max_length=100, choices=choices, default=None )
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=250, default=None)
    v_email = models.CharField(max_length=400)
    
    def __str__(self):
        return self.event + " : " + self.first_name + " " + self.last_name