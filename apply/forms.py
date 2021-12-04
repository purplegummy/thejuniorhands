from django.forms import ModelForm
from .models import Applicant
from django.utils.translation import ugettext_lazy as _


class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
  
        
        
        