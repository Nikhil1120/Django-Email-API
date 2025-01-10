from django.urls import path
from .views import *
urlpatterns = [
    path('web_mail', send_mail_web),
    path('API_mail', send_email_API),
]
