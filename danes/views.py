from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
    context = {}
    return render_to_response("home.html", context)
