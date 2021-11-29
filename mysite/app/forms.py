from django.forms import ModelForm
from .models import Contact, Subscription, Volunteer
from django.utils.translation import ugettext_lazy as _


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
  
class EmailForm(ModelForm):
    class Meta:
        model = Subscription
        fields='__all__'

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = '__all__'
        