from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UploadForm

def index(request):
    return HttpResponse("This string represents the content of the httpresponse")

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
    else:
        form = UploadForm()

    return render(request, 'upload.html', {form: form})

