from django.urls import path

from . import views


urlpatterns = [
    path('basic', views.basic_passphrase, name='basic_passphrase'),
    path('advance', views.advance_passphrase, name='advance_passphrase')
]