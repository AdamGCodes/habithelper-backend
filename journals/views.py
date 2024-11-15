from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from utils.exceptions import handle_exceptions
from .serializers import JournalSerializer
from .models import Journal

# Create your views here.

class ListCreateJournalView(APIView):
    permission_classes = [IsAuthenticated]
    # Index Controller
    # GET /journals/
    @handle_exceptions
    def get(self, request):
        journals= Journal.objects.filter(author=request.user.id)
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)

    # Create Controller
    # POST /journals/
    @handle_exceptions
    def post(self, request):
        request.data['author'] = request.user.id
        new_journal = JournalSerializer(data=request.data)
        new_journal.is_valid(raise_exception=True)
        new_journal.save()
        return Response(new_journal.data, status.HTTP_201_CREATED)


class RetrieveUpdateDestroyJournalView(APIView):
    permission_classes = [IsAuthenticated]
    # Show Controller
    # GET /journals/:pk/
    @handle_exceptions
    def get(self, request, pk):
        journal = Journal.objects.filter(author=request.user.id).get(pk=pk)
        serializer = JournalSerializer(journal)
        return Response(serializer.data)

    # Delete Controller
    # DELETE /journals/:pk/

    @handle_exceptions
    def delete(self, request, pk):
        journal = Journal.objects.filter(author=request.user.id).get(pk=pk)
        self.check_object_permissions(request, journal)
        journal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Update Controller
    # PUT /journals/:pk/
    @handle_exceptions
    def put(self, request, pk):
        journal = Journal.objects.filter(author=request.user.id).get(pk=pk)
        self.check_object_permissions(request, journal)

        serializer = JournalSerializer(journal, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
