from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This string represents the content of the httpresponse")
