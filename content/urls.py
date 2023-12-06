from django.urls import path
from .views import Homepage, MailContact

urlpatterns = [
    path('',Homepage, name="index"),
    path('contact/',MailContact, name="contact"),
]
