
from django.forms import ModelForm
from django.forms.widgets import TextInput
from sauceprotecc.models import Image

class UploadForm(ModelForm):
    
    class Meta:
        model = Image
        URLfield = ('post_location',)
        fields = ('description',)




# from django.forms import ModelForm
# from .models import Image

# class ImageForm(ModelForm):
#     class Meta:
#         model = Image
#         fields = ('post_location', 'description',)

  