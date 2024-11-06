from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, UserSerializer, SignInSerializer
from .helpers import send_mail_to_user

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        current_site = get_current_site(request)
        mail_template_context = {
            'name': user.first_name,
            'domain': current_site.domain,
            'token': token,
            'uid': urlsafe_base64_encode(force_bytes(user.pk))
        }
        mail_subject = "Confirm your Email @ BuyAnything.com"
        mail_template_name = 'activation_mail.html'
        send_mail_to_user(user, mail_subject, mail_template_name, mail_template_context)

        return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def signin(request):
    # user = get_object_or_404(User, username=request.data['username'])
    # if user.check_password(request.data['password']):
    # serializer = SignInSerializer(request.data)
    # if serializer.is_valid():
    user = authenticate(username=request.data['username'], password=request.data['password'])
    if not user:
        return Response({"error": "Invalid Credentials!"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    if not token:
        token = created
        
    login(request, user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)




@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed!")

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def signout(request):
    token_value = request.headers['Authorization']
    key = token_value.split(' ')[-1]
    user = Token.objects.get(key=key).user
    Token.objects.filter(user=user).delete()
    logout(request)
    return Response({"success":"Logged out successfully"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user:
        try:
            user = Token.objects.get(key=token).user
        except:
            user = None

    if user is not None:
        user.is_active = True
        user.save()
        mail_subject = "Account activated @ BuyAnything.com"
        mail_template_name = 'email_confirmation.html'
        send_mail_to_user(user, mail_subject, mail_template_name, {})
        return Response({'success': 'Account Activated'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid activation link'}, status=status.HTTP_400_BAD_REQUEST)

