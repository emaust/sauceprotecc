from django.test import TestCase
from sauceprotecc.models import Image
from django.utils import timezone
from django.urls import reverse
from sauceprotecc.forms import UploadForm

class ImageModelTest(TestCase):

    def create_image(self, file_name="raccoontest", image_address="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Raccoon_climbing_in_tree_-_Cropped_and_color_corrected.jpg/1024px-Raccoon_climbing_in_tree_-_Cropped_and_color_corrected.jpg", date_posted=timezone.now()):
        return Image.objects.create(file_name=file_name, image_address=image_address, date_posted=date_posted)

    def test_image_creation(self):
        i = self.create_image()
        self.assertTrue(isinstance(i, Image))
        self.assertEqual(i.__str__(), i.file_name)