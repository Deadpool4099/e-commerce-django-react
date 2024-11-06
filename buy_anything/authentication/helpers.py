from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings


def send_mail_to_user(user, mail_subject, mail_template_name, mail_template_context):

    # Email Address Confirmation Email
    message = render_to_string(mail_template_name, mail_template_context)
    email = EmailMessage(
        mail_subject,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
    )
    email.fail_silently = True
    email.send()
    
    # current_site = get_current_site(request)
    # email_subject = "Confirm your Email @ BuyAnything.com"
    # message2 = render_to_string('activation_mail.html', {
    #     'name': user.first_name,
    #     'domain': current_site.domain,
    #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #     'token': token
    # })
    # email = EmailMessage(
    #     email_subject,
    #     message2,
    #     settings.EMAIL_HOST_USER,
    #     [user.email],
    # )
    # email.fail_silently = True
    # email.send()
    