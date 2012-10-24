from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.conf import settings
from registrations.models import RegistrationForm

import stripe, os
from stripe import CardError
from django.core.mail import send_mail
from django.template.loader import render_to_string

def clinic_register(request):
    template, context = register(request, settings.CLINIC)
    return render_to_response(template, context)

def show_register(request):
    template, context = register(request, settings.SHOWCASE)
    return render_to_response(template, context)

def winter_register(request):
    template, context = register(request, settings.WINTER)
    return render_to_response(template, context)

def register(request, reg_type):
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
            #stripe.api_key = os.environ['STRIPE_TEST_SECRET']
            stripe.api_key = os.environ['STRIPE_SECRET']
            if 'price' in request.POST:
                price = request.POST['price']
            else:
                price = reg_type['price']
            try:
                charge = stripe.Charge.create(
                    amount=int(price)*100,                              
                    currency="usd",
                    card=token,
                    description=reg_type['description'] + " Registration: " + request.POST['firstName']+ " " + request.POST['lastName']
                    )
                SUBJECT = reg_type['subject']
                FROM = "UAlbany Baseball <confirmation@juniordanesbaseballacademy.com>"
                MESSAGE = render_to_string(reg_type['email_template'], context)
                CUSTOMER = [request.POST['email']]
                DIRECTOR = ['jkaier@albany.edu']
                send_mail(SUBJECT, MESSAGE, FROM, CUSTOMER, fail_silently=False)
                send_mail(SUBJECT, MESSAGE, FROM, DIRECTOR, fail_silently=False)
                registration = registration_form.save(commit=False)
                registration.type=reg_type['description']
                registration.save()
                return reg_type['success_url'], context
            except CardError as e:
                context['card_error'] = e.message
                return "failure.html", context
        else:
            context['invalid'] = True

    context['registration_form'] = registration_form
    return reg_type['base_url'], context

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

def clinics(request):
    context = {}
    return render_to_response("clinics.html", context)

def reg_closed(request):
    context = {}
    return render_to_response("reg_closed.html", context)
