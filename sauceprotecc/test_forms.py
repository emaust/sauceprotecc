from sauceprotecc.forms import UploadForm
from sauceprotecc.models import Image

def test_valid_form(self):
    i = Image.objects.create(image_name="bojack", image_address="https://cdn.vox-cdn.com/thumbor/Z6A-QDFwnLZEzHFqyaG3pl69OQA=/0x0:1200x673/1220x813/filters:focal(504x241:696x433):format(webp)/cdn.vox-cdn.com/uploads/chorusimage/image/57200569/bojack.0.0.jpg")
    data = {'image_name': i.image_name, i.image_address:"https://cdn.vox-cdn.com/thumbor/Z6A-QDFwnLZEzHFqyaG3pl69OQA=/0x0:1200x673/1220x813/filters:focal(504x241:696x433):format(webp)/cdn.vox-cdn.com/uploads/chorusimage/image/57200569/bojack.0.0.jpg"}
    form = UploadForm(data=data)
    self.assertTrue(form.is_valid())

def test_invalid_form(self):
    i = Image.objects.create(image_name="typicalhorse", image_address="potato")
    data = {'image_name': i.image_name, 'image_address': i.image_address,}
    form = UploadForm(data=data)
    self.assertFalse(form.is_valid())