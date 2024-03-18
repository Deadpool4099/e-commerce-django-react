
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from .tokens import generate_token


def send_activation_mail(request, myuser, token):

    # Email Address Confirmation Email
    current_site = get_current_site(request)
    email_subject = "Confirm your Email @ BuyAnything.com - Django Login!!"
    message2 = render_to_string('email_confirmation.html', {
        'name': myuser.first_name,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token': token
    })
    email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
    )
    email.fail_silently = True
    email.send()