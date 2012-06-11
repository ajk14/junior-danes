from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from registrations.models import RegistrationForm
import stripe, os
from stripe import CardError

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
            stripe.api_key = os.environ['stripe_private']
            try:
                charge = stripe.Charge.create(
                    amount=20000, # amount in cents
                    currency="usd",
                    card=token,
                    description="payinguser@example.com"
                    )
                registration_form.save()
                return render_to_response("success.html", context)
            except CardError as e:
                context['card_error'] = e.message
                return render_to_response("failure.html", context)
        else: context['invalid'] = True

    context['registration_form'] = registration_form
    return render_to_response("form.html", context)
