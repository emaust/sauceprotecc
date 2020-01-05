from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect 
from sauceprotecc.forms import UploadForm
from sauceprotecc.models import Image
from django.core.exceptions import ValidationError


class UploadImage(forms.Form):

    model = Image
    fields = '__all__'

def index(request):
    return HttpResponse("Home page")

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('/upload/')
        else:
          for e in form.errors['file_name'].as_data():
            print(e)
          # [u'Image name must be unique. testing']
        #     raise forms.ValidationError('Address must be a url')
          # print(form)
    else:
        form = UploadForm()
    return render(request, 'upload.html', {form: form})

def results(request):
    return HttpResponse("Results page")

def profile(request):
    return HttpResponse("Profile page")

def login(request):
    return HttpResponse("Login page")
