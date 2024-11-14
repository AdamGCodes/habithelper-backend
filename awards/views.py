from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.exceptions import handle_exceptions
from .models import Award

# Create your views here.


class ListCreateAwardView(APIView):

    # Index Controller
    # GET /awards/
    @handle_exceptions
    def get(self, request):

        return Response('HIT INDEX ROUTE')

    # Create Controller
    # POST /awards/
    @handle_exceptions
    def post(self, request):

        return Response('HIT CREAT ROUTE')


class RetrieveUpdateDestroyAwardView(APIView):

    # Show Controller
    # GET /awards/:pk/
    @handle_exceptions
    def get(self, request, pk):

        return Response('HIT SHOW ROUTE')

    # Delete Controller
    # DELETE /awards/:pk/

    @handle_exceptions
    def delete(self, request, pk):

        return Response('HIT DELETE ROUTE')

    # Update Controller
    # PUT /awards/:pk/
    @handle_exceptions
    def put(self, request, pk):

        return Response('HIT UPDATE ROUTE')
