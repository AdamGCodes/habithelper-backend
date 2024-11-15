from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from utils.exceptions import handle_exceptions
from .serializers import Habit_HelperSerializer
from .models import Habit_Helper

# Create your views here.


class ListCreateHabit_HelperView(APIView):
    permission_classes = [IsAuthenticated]
    # Index Controller
    # GET /habit_helpers/
    @handle_exceptions
    def get(self, request):
        habit_helpers = Habit_Helper.objects.filter(user=request.user.id)
        serializer = Habit_HelperSerializer(habit_helpers, many=True)
        return Response(serializer.data)

    # Create Controller
    # POST /habit_helpers/
    @handle_exceptions
    def post(self, request):
        request.data['user'] = request.user.id
        new_habit_helper = Habit_HelperSerializer(data=request.data)
        new_habit_helper.is_valid(raise_exception=True)
        new_habit_helper.save()
        return Response(new_habit_helper.data, status.HTTP_201_CREATED)


class RetrieveUpdateDestroyHabit_HelperView(APIView):
    permission_classes = [IsAuthenticated]

    # Show Controller
    # GET /habit_helpers/:pk/
    @handle_exceptions
    def get(self, request, pk):
        habit_helper = Habit_Helper.objects.filter(user=request.user.id).get(pk=pk)
        serializer = Habit_HelperSerializer(habit_helper)
        return Response(serializer.data)

    # Delete Controller
    # DELETE /habit_helpers/:pk/

    @handle_exceptions
    def delete(self, request, pk):
        habit_helper = Habit_Helper.objects.filter(user=request.user.id).get(pk=pk)
        self.check_object_permissions(request, habit_helper)
        habit_helper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Update Controller
    # PUT /habit_helpers/:pk/
    @handle_exceptions
    def put(self, request, pk):
        habit_helper = Habit_Helper.objects.filter(user=request.user.id).get(pk=pk)
        self.check_object_permissions(request, habit_helper)

        serializer = Habit_HelperSerializer(habit_helper, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
