# Import DRF modules
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Import DRF serializers
from .serializers import UserSerializer

# Import Django authentication
from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import force_bytes, force_str
# Import Django User model
from django.contrib.auth.models import User

# Import Django messages framework
from django.contrib import messages

# Import other necessary modules
from .tokens import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


from django.shortcuts import render

class HomeView(APIView):
    def get(self, request):
        return render(request, 'authentication/index.html')
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

class SignupView(View):
    def get(self, request):
        return render(request, "authentication/signup.html")

    def post(self, request):
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! Please try another username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords don't match!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your account has been created successfully! Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email
        subject = "Welcome to BuyAnything.com - Django Login!!"
        message = f"Hello {myuser.first_name}!\nWelcome to BuyAnything.com!\nThank you for visiting our website. We have also sent you a confirmation email, please confirm your email address.\n\nThank you,\n"
        from_email = settings.EMAIL_HOST_USER
        to_email = [myuser.email]
        send_mail(subject, message, from_email, to_email, fail_silently=True)

        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ BuyAnything.com - Django Login!!"
        message2 = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('signin')


class ActivateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, "Your Account has been activated!!")
            return redirect('signin')
        else:
            return Response({'error': 'Invalid activation link'}, status=status.HTTP_400_BAD_REQUEST)

class SigninView(View):
    def get(self, request):
        return render(request, "authentication/signin.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

class SignoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged Out Successfully!")
        return redirect('home')
