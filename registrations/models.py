from django.db import models
from django.forms import ModelForm, Textarea, TextInput
from django.contrib.localflavor.us.forms import USPhoneNumberField, USStateField, USZipCodeField, USStateSelect, USPSSelect
from django.contrib.localflavor.us.models import PhoneNumberField, USPostalCodeField
from django.contrib.localflavor.us.models import *
from django.forms.extras.widgets import SelectDateWidget

class Registration(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    height = models.CharField(max_length=20)
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

    def __unicode__(self):
        return u'%s %s' % (self.firstName, self.lastName)

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
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
            'position':TextInput(attrs={'placeholder': 'Position'}),
            'email':TextInput(attrs={'placeholder': 'E-mail'}),
            }

class ShowcaseRegistration(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
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
    dates = models.IntegerField()
    school = models.CharField(max_length=100)
    gradYear = models.CharField(max_length=4)

    def __unicode__(self):
        return u'%s %s'% (self.firstName, self.lastName)

class ShowcaseRegistrationForm(ModelForm):
    class Meta:
        model = ShowcaseRegistration
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
            }

