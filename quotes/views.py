from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.exceptions import handle_exceptions
from .models import Quote

# Create your views here.


class ListCreateQuoteView(APIView):

    # Index Controller
    # GET /quotes/
    @handle_exceptions
    def get(self, request):

        return Response('HIT INDEX ROUTE')

    # Create Controller
    # POST /quotes/
    @handle_exceptions
    def post(self, request):

        return Response('HIT CREAT ROUTE')


class RetrieveUpdateDestroyQuoteView(APIView):

    # Show Controller
    # GET /quotes/:pk/
    @handle_exceptions
    def get(self, request, pk):

        return Response('HIT SHOW ROUTE')

    # Delete Controller
    # DELETE /quotes/:pk/

    @handle_exceptions
    def delete(self, request, pk):

        return Response('HIT DELETE ROUTE')

    # Update Controller
    # PUT /quotes/:pk/
    @handle_exceptions
    def put(self, request, pk):

        return Response('HIT UPDATE ROUTE')
