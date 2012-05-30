from django.shortcuts import render_to_response
from django.http import HttpResponse

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
