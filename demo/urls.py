from django.urls import path
from . import views

urlpatterns = [
    path('' , views.some_demo , name='some_demo'),
]
