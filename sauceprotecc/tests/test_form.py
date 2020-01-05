from sauceprotecc.forms import UploadForm
from sauceprotecc.models import Image
from django.test import TestCase
from django.test import Client
from django.utils import timezone


# class UploadFormTest(TestCase):

#   def test_valid_address(self):
#       t=timezone.now()
#       i = Image.objects.create(file_name="bojack", image_address="https://cdn.vox-cdn.com/thumbor/Z6A-QDFwnLZEzHFqyaG3pl69OQA=/0x0:1200x673/1220x813/filters:focal(504x241:696x433):format(webp)/cdn.vox-cdn.com/uploads/chorusimage/image/57200569/bojack.0.0.jpg", date_posted=t
#       data = {'image_name': i.file_name, 'image_address': i.image_address, 'date_posted':i.date_posted}
#       form = UploadForm(data=data)
#       self.assertTrue(form.is_valid())

#   def test_invalid_address(self):
#       i = Image.objects.create(file_name="typicalhorse", image_address="potato")
#       data = {'image_name': i.file_name, 'image_address': i.image_address,}
#       form = UploadForm(data=data)
#       self.assertFalse(form.is_valid())

#   def test_unique_name(self):
#       image1 = Image.objects.create(image_name="bojack")
#       # image2 = Image.objects.create(image_name="bojack")
#       data = {'image_name': image1.image_name}
#       form = UploadForm(data=data)
#       self.assertFalse(form.is_valid())