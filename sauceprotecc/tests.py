from django.test import SimpleTestCase
from django.test import TestCase
from django.http import HttpRequest
from . import views

class IndexPageTests(SimpleTestCase):
  def test_index_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)
  # def test_view_uses_correct_template(self):
  #       response = self.client.get('/')
  #       self.assertEquals(response.status_code, 200)
  #       self.assertTemplateUsed(response, 'index.html')


class UploadPageTests(SimpleTestCase):
  def test_upload_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)
  # def test_view_uses_correct_template(self):
  #       response = self.client.get('/')
  #       self.assertEquals(response.status_code, 200)
  #       self.assertTemplateUsed(response, 'upload.html')


class ResultsPageTests(SimpleTestCase):
  def test_results_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)
  # def test_view_uses_correct_template(self):
  #       response = self.client.get('/')
  #       self.assertEquals(response.status_code, 200)
  #       self.assertTemplateUsed(response, 'results.html')


class LoginPageTests(SimpleTestCase):
  
  def test_login_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)
  # def test_view_uses_correct_template(self):
  #       response = self.client.get('/')
  #       self.assertEquals(response.status_code, 200)
  #       self.assertTemplateUsed(response, 'login.html')


class ProfilePageTests(SimpleTestCase):
  
  def test_index_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)
  # def test_view_uses_correct_template(self):
  #       response = self.client.get('/')
  #       self.assertEquals(response.status_code, 200)
  #       self.assertTemplateUsed(response, 'login.html')
