from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from registrations.models import RegistrationForm, ShowcaseRegistrationForm
import stripe, os
from stripe import CardError
from django.core.mail import send_mail
from django.template.loader import render_to_string

def home(request):
    context = {}
    return render_to_response("home.html", context)

def winter(request):
    context = {}
    return render_to_response("winter.html", context)

def summer(request):
    context = {}
    return render_to_response("summer.html", context)

def showcases(request):
    context = {}
    return render_to_response("showcases.html", context)

def reg_closed(request):
    context = {}
    return render_to_response("reg_closed.html", context)

def showregister(request):
    context = {}
    context['invalid'] = False
    context.update(csrf(request))
    registration_form = ShowcaseRegistrationForm()
    if request.method == "POST":
        registration_form = ShowcaseRegistrationForm(request.POST)
        if registration_form.is_valid():
            context = request.POST.copy()
            context.update(csrf(request))
            token = request.POST['stripeToken']
            stripe.api_key = os.environ['STRIPE_SECRET']
            try:
                charge = stripe.Charge.create(
                    amount=12500, # amount in cents                              
                    currency="usd",
                    card=token,
                    description="Showcase Registration: " + request.POST['firstName']+ " " + request.POST['lastName']
                    )
                SUBJECT = "UAlbany Baseball Prospect Showcase Registration Confirmation"
                FROM = "UAlbany Baseball <confirmation@juniordanesbaseballacademy.com>"
                MESSAGE = render_to_string('showcase_email.txt', context)
                CUSTOMER = [request.POST['email']]
                DIRECTOR = ['jkaier@albany.edu']
                send_mail(SUBJECT, MESSAGE, FROM, CUSTOMER, fail_silently=False)
                send_mail(SUBJECT, MESSAGE, FROM, DIRECTOR, fail_silently=False)
                registration_form.save()
                return render_to_response("showcase_success.html", context)
            except CardError as e:
                context['card_error'] = e.message
                return render_to_response("failure.html", context)
        else:
            context['invalid'] = True

    context['registration_form'] = registration_form
    return render_to_response("showform.html", context)

def register(request):
    context = {}
    context['invalid'] = False
    context.update(csrf(request))
    registration_form = RegistrationForm()
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            context = request.POST.copy()
            context.update(csrf(request))
            token = request.POST['stripeToken']
            stripe.api_key = os.environ['STRIPE_SECRET']
            try:
                charge = stripe.Charge.create(
                    amount=20000, # amount in cents
                    currency="usd",
                    card=token,
                    description="Camp Registration: " + request.POST['firstName']+ " " + request.POST['lastName']
                    )
                SUBJECT = "Junior Danes Baseball Academy Registration Confirmation"
                FROM = "Junior Danes Baseball <confirmation@juniordanesbaseballacademy.com>"
                MESSAGE = render_to_string('email.txt', context)
                CUSTOMER = [request.POST['email']]
                DIRECTOR = ['jkaier@albany.edu']
                send_mail(SUBJECT, MESSAGE, FROM, CUSTOMER, fail_silently=False)
                send_mail(SUBJECT, MESSAGE, FROM, DIRECTOR, fail_silently=False)
                registration_form.save()
                return render_to_response("success.html", context)
            except CardError as e:
                context['card_error'] = e.message
                return render_to_response("failure.html", context)
        else: 
            context['invalid'] = True

    context['registration_form'] = registration_form
    return render_to_response("form.html", context)
