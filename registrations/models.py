from django.db import models
from django.forms import ModelForm, Textarea, TextInput, RadioSelect
from django.contrib.localflavor.us.forms import USPhoneNumberField, USStateField, USZipCodeField, USStateSelect, USPSSelect
from django.contrib.localflavor.us.models import PhoneNumberField, USPostalCodeField
from django.contrib.localflavor.us.models import *
from django.forms.extras.widgets import SelectDateWidget
from django.utils.safestring import mark_safe

class HorizRadioRenderer(RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class Registration(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField()
    email = models.EmailField()
    position = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = USPostalCodeField()
    zip = models.CharField(max_length=5)
    phone = PhoneNumberField()
    cell = PhoneNumberField()
    parentName = models.CharField(max_length=200)
    emergencyContact = PhoneNumberField()
    emergencyName = models.CharField(max_length=200)
    relationship = models.CharField(max_length=100)
    dates = models.IntegerField(null=True, blank=True)
    school = models.CharField(max_length=100, null=True, blank=True)
    gradYear = models.CharField(max_length=4, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    program = models.CharField(max_length=100, null=True, blank=True)
    hit_time = models.CharField(max_length=100, null=True, blank=True)
    field_time = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
   
    def __unicode__(self):
        return u'%s %s'% (self.firstName, self.lastName)

CHOICES = (('hit', 'Hitting Only ($189)'), ('def', 'Defense/Pitching Only ($189)'), ('both', 'Hitting and Defense/Pitching ($249)'))
HIT_TIME = (('4-5 PM', '4-5 PM'), ('5-6 PM', '5-6 PM'), ('6-7 PM', '6-7 PM'))
FIELD_TIME = (('7-8 PM', '7-8 PM'),)

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        exclude = ('type',)
        widgets = {
            'state':USPSSelect(),
            'firstName':TextInput(attrs={'placeholder': 'First'}),
            'lastName':TextInput(attrs={'placeholder': 'Last'}),
            'address':TextInput(attrs={'placeholder': 'Street'}),
            'city':TextInput(attrs={'placeholder': 'City'}),
            'zip':TextInput(attrs={'placeholder': 'Zip'}),
            'parentName':TextInput(attrs={'placeholder': 'Name'}),
            'emergencyName':TextInput(attrs={'placeholder': 'Name'}),
            'relationship':TextInput(attrs={'placeholder': 'Relationship'}),
            'phone':TextInput(attrs={'placeholder': 'Home Phone'}),
            'cell':TextInput(attrs={'placeholder': 'Cell'}),
            'emergencyContact':TextInput(attrs={'placeholder': 'Phone'}),
            'age':TextInput(attrs={'placeholder': 'Age'}),
            'height':TextInput(attrs={'placeholder': 'Height'}),
            'position':TextInput(attrs={'placeholder': 'Position(s)'}),
            'email':TextInput(attrs={'placeholder': 'E-mail'}),
            'weight':TextInput(attrs={'placeholder': 'Weight'}),
            'school':TextInput(attrs={'placeholder': 'School'}),
            'gradYear':TextInput(attrs={'placeholder': 'Year'}),
            'program':RadioSelect(renderer=HorizRadioRenderer, choices = CHOICES), 
            'hit_time':RadioSelect(renderer=HorizRadioRenderer, choices = HIT_TIME),
            'field_time':RadioSelect(renderer=HorizRadioRenderer, choices = FIELD_TIME),
            }

