from django.contrib import admin
from django.urls import path
from .views import index
from .views import upload
from .views import results
from .views import login
from .views import profile
# from . import views


urlpatterns = [
  path('admin', admin.site.urls),
  path('', index),
  path('upload/', upload),
  path('results/', results),
  path('login/', login),
  path('profile/', profile),
  
]

# path() '/', views.index, name='index',

