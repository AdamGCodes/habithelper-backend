from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from utils.exceptions import handle_exceptions
from .serializers import QuoteSerializer
from .models import Quote

# Create your views here.


class ListCreateQuoteView(APIView):
    permission_classes = [IsAuthenticated]
    # Index Controller
    # GET /quotes/

    @handle_exceptions
    def get(self, request):
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    # Create Controller
    # POST /quotes/
    @handle_exceptions
    def post(self, request):
        request.data['author'] = request.user.id
        new_quote = QuoteSerializer(data=request.data)
        new_quote.is_valid(raise_exception=True)
        new_quote.save()
        return Response(new_quote.data, status.HTTP_201_CREATED)


class RetrieveUpdateDestroyQuoteView(APIView):
    permission_classes = [IsAuthenticated]
    # Show Controller
    # GET /quotes/:pk/

    @handle_exceptions
    def get(self, request, pk):
        quote = Quote.objects.filter(author=request.user.id).get(pk=pk)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)

    # Delete Controller
    # DELETE /quotes/:pk/

    @handle_exceptions
    def delete(self, request, pk):
        quote = Quote.objects.filter(author=request.user.id).get(pk=pk)
        self.check_object_permissions(request, quote)
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Update Controller
    # PUT /quotes/:pk/
    @handle_exceptions
    def put(self, request, pk):
        quote = Quote.objects.filter(author=request.user.id).get(pk=pk)
        self.check_object_permissions(request, quote)

        serializer = QuoteSerializer(
            quote, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
