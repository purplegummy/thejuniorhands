from django.db import models
from django.core.validators import EMPTY_VALUES, validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
GENDER_CHOICES = [
    ('space', ''),
    ('male', 'Male'),
    ('female', 'Female'),
    ('nonbinary', 'Nonbinary'),
    ('other', 'Other')
]

GRADE_CHOICES = [
    (None, 'Choose a Gender'),
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior')
]
DAYS = []
YEARS = []
for i in range(1, 32):
    DAYS.append((str(i), str(i)))

for i in range (1920, 2022):
    YEARS.append((i, i))

MONTHS = [
    ('None', ' '),
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
print(YEARS)
# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[validate_email])
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default=None, blank=False)
    grade  = models.CharField(max_length=100, choices=GRADE_CHOICES, default=None, blank=True)
    school = models.CharField(max_length=100, blank=True)
    birthday = models.CharField(max_length=30, choices=DAYS, default=None, blank=True)
    birthmonth = models.CharField(max_length=30, choices=MONTHS, default=None, blank=True)
    birthyear = models.IntegerField(default=None, choices=YEARS, blank=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    county = models.CharField(max_length=100, default=None)
    zip_code = models.IntegerField()
    check = models.BooleanField(default=False)
    readCheck = models.BooleanField(default=False)

    
    
    def __str__(self):
        return self.first_name + " " + self.last_name


            
       