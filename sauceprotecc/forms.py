
import datetime
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from sauceprotecc.models import Image

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'post_location',)

form = UploadForm()
    