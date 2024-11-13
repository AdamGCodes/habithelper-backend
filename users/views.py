from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

class SignUpView(APIView):
    def post(self, request):
        return Response("Hit SignUp Route")
    

class SignInView(APIView):
    def post(self, request):
        return Response("Hit SignIn Route")