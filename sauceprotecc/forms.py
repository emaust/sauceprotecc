
import datetime
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from sauceprotecc.models import Image

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description',)

form = UploadForm()
    # description = models.CharField()

    # def clean_description(self):
    #     data = self.cleaned_data['description']
    #     return data
#     data = {'description': 'hello',
# ...         'message': 'Hi there',
# ...         'sender': 'foo@example.com',
# ...         'cc_myself': True}
# >>> f = ContactForm(data)
#     date_posted = forms.DateField(initial=datetime.date.today())
#     post_location = forms.URLField(initial="http://", widget=TextInput)
#     description = forms.CharField()

#     class Meta:
#         model = Image
#         fields = '__all__'

#     def upload(self):
#         pass




# from django.forms import ModelForm
# from .models import Image

# class ImageForm(ModelForm):
#     class Meta:
#         model = Image
#         fields = ('post_location', 'description',)

  