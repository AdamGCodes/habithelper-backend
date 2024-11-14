from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.exceptions import handle_exceptions
from .models import Timer

# Create your views here.
class ListCreateTimerView(APIView):

    #Index Controller
    #GET /timers/
    @handle_exceptions
    def get(self,request):
        
        return Response('HIT INDEX ROUTE')
    
    #Create Controller
    #POST /timers/
    @handle_exceptions
    def post(self, request):

        return Response('HIT CREAT ROUTE')
    

class RetrieveUpdateDestroyTimerView(APIView):

    #Show Controller
    #GET /timers/:pk/
    @handle_exceptions
    def get(self, request, pk):

        return Response('HIT SHOW ROUTE')
    

    #Delete Controller
    #DELETE /timers/:pk/
    @handle_exceptions
    def delete(self, request, pk):

        return Response('HIT DELETE ROUTE')
    
    # Update Controller
    # PUT /timers/:pk/
    @handle_exceptions
    def put(self, request, pk):

        return Response('HIT UPDATE ROUTE')
