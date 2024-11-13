#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q

from .serializers import UserSerializer
from utils.exceptions import handle_exceptions

from django.contrib.auth import get_user_model, hashers
User = get_user_model()


# Create your views here.

class SignUpView(APIView):
    @handle_exceptions
    def post(self, request):
        new_user = UserSerializer(data=request.data)
        new_user.is_valid(raise_exception=True)
        new_user.save()
        return Response({
            'message': 'Signup successful',
            'user': new_user.data
        })
    

class SignInView(APIView):
    @handle_exceptions
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        #Identify the user by email (why it's unique)
        user = User.objects.get(email=email)

        #Compare entered password and hashed stored password
        if hashers.check_password(password, user.password):
            #Generate token
            token_pair = RefreshToken.for_user(user)

            serialized_user = UserSerializer(user)

            return Response({
                'user': serialized_user.data,
                'token' : str(token_pair.access_token)
            })
    
        return Response({ ' detail' : 'Unauthorized'}, status.HTTP_401_UNAUTHORIZED)