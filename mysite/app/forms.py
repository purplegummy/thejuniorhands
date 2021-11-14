from django.forms import ModelForm
from .models import Contact, Subscription
from django.utils.translation import ugettext_lazy as _


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
  
class EmailForm(ModelForm):
    class Meta:
        model = Subscription
        fields='__all__'