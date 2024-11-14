from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.exceptions import handle_exceptions
from .models import Journal

# Create your views here.

class ListCreateJournalView(APIView):

    # Index Controller
    # GET /journals/
    @handle_exceptions
    def get(self, request):

        return Response('HIT INDEX ROUTE')

    # Create Controller
    # POST /journals/
    @handle_exceptions
    def post(self, request):

        return Response('HIT CREAT ROUTE')


class RetrieveUpdateDestroyJournalView(APIView):

    # Show Controller
    # GET /journals/:pk/
    @handle_exceptions
    def get(self, request, pk):

        return Response('HIT SHOW ROUTE')

    # Delete Controller
    # DELETE /journals/:pk/

    @handle_exceptions
    def delete(self, request, pk):

        return Response('HIT DELETE ROUTE')

    # Update Controller
    # PUT /journals/:pk/
    @handle_exceptions
    def put(self, request, pk):

        return Response('HIT UPDATE ROUTE')
