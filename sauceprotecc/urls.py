from django.urls import path
from . import views


urlpatterns = [
  # path('upload', views.index, name='index'),
  path('upload/', views.upload_image),
]


