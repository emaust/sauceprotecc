import datetime
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from sauceprotecc.models import Image
from django.core.exceptions import ValidationError

class UploadForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('description', 'image_address', 'whitelist', 'file_name',)

    
    def clean(self):
        cleaned_data = super(UploadForm, self).clean()
        return cleaned_data



        # file_name = self.cleaned_data["file_name"]
        # if Image.objects.filter(file_name=file_name).exists():
        #     raise forms.ValidationError("The image you are uploading already exists in the database.")
        # return file_name
    # def clean(self):
    #     data = self.cleaned_data

    #     x = data.get('description')
    #     print(data)


    #     check1="http://"
    #     check2="https://"
    #     address = data.get('image_address')

    #     if 'image_address' in data.keys() and check1 not in data['image_address'] and check2 not in data['image_address']:
    #         raise forms.ValidationError('Address must be a url')

form = UploadForm()
    