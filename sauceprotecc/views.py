from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
# from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
# from django.urls import 
from sauceprotecc.forms import UploadForm
from sauceprotecc.models import Image

class UploadImage(forms.Form):
# class upload()
    model = Image
    fields = '__all__'

def index(request):
    return HttpResponse("This string represents the content of the httpresponse")

def upload(request):
    # form = UploadForm()
    # print(request.method)
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('/upload/')

    else:
        form = UploadForm()
    return render(request, 'upload.html', {form: form})

