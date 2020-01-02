from django import forms

class UploadForm(forms.Form):
  post_location = forms.URLField



# from django.forms import ModelForm
# from .models import Image

# class ImageForm(ModelForm):
#     class Meta:
#         model = Image
#         fields = ('post_location', 'description',)

  