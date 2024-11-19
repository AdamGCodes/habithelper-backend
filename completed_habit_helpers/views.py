from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from utils.exceptions import handle_exceptions
from .serializers import Completed_Habit_HelperSerializer
from .models import Completed_Habit_Helper

# Create your views here.

class ListCreateCompleted_Habit_HelperView(APIView):
    permission_classes = [IsAuthenticated]
    # Index Controller
    # GET /awards/
    @handle_exceptions
    def get(self, request):
        completed_habit_helpers = Completed_Habit_Helper.objects.filter(user=request.user.id)
        serializer = Completed_Habit_HelperSerializer(completed_habit_helpers, many=True)
        return Response(serializer.data)


    # Create Controller
    # POST /awards/
    @handle_exceptions
    def post(self, request):

        return Response('HIT CREAT ROUTE')


class RetrieveUpdateDestroyCompleted_Habit_HelperView(APIView):
    permission_classes = [IsAuthenticated]
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
