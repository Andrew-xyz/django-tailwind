from django.urls import path

from splash.views import index

urlpatterns = [
    path('', index),
]
