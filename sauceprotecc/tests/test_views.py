from django.test import SimpleTestCase
from django.test import TestCase
from django.test import Client
from django.http import HttpRequest
from sauceprotecc import views

class IndexPageTests(SimpleTestCase):
  def test_index_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)


class UploadPageTests(SimpleTestCase):
  def test_upload_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)


class ResultsPageTests(SimpleTestCase):
  def test_results_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)


class LoginPageTests(SimpleTestCase):
  
  def test_login_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)
  

class ProfilePageTests(SimpleTestCase):
  
  def test_index_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)
  

