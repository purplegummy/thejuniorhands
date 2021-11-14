from django.db import models

class upcomingEvent(models.Model):
    eventName = models.CharField(max_length=200)
    day = models.CharField(max_length=15)
    month = models.CharField(max_length=3)
    location = models.CharField(max_length=200)

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