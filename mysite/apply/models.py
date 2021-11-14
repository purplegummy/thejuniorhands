from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('nonbinary', 'Nonbinary'),
    ('other', 'Other')
]

GRADE_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior')
]
DAYS = []
for i in range(1, 32):
    DAYS.append((str(i), str(i)))

MONTHS = [
    ('january', 'January'),
    ('february', 'February'),
    ('march', 'March'),
    ('april', 'April'),
    ('may', 'May'),
    ('june', 'June'),
    ('july', 'July'),
    ('august', 'August'),
    ('september', 'September'),
    ('october', 'October'),
    ('november', 'November'),
    ('december', 'December'),

]
# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[validate_email])
    phone = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default=None)
    grade  = models.CharField(max_length=100, choices=GRADE_CHOICES, default=None)
    school = models.CharField(max_length=100)
    birthday = models.CharField(max_length=30, choices=DAYS, default=None)
    birthmonth = models.CharField(max_length=30, choices=MONTHS, default=None)
    birthyear = models.IntegerField(default=None)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    check = models.BooleanField()
    readCheck = models.BooleanField()
    
    def __str__(self):
        return self.first_name + " " + self.last_name


            
       