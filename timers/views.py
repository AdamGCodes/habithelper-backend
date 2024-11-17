from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .serializers import TimerSerializer
from utils.exceptions import handle_exceptions
from .models import Timer


# Create your views here.
class ListCreateTimerView(APIView):
    permission_classes = [IsAuthenticated]
    #Index Controller
    #GET /timers/
    @handle_exceptions
    def get(self,request):
        timers = Timer.objects.filter(user=request.user.id)
        serializer = TimerSerializer(timers, many=True)
        return Response(serializer.data)
    
    #Create Controller
    #POST /timers/
    @handle_exceptions
    def post(self, request):
        request.data['user'] = request.user.id
        new_timer = TimerSerializer(data=request.data)
        new_timer.is_valid(raise_exception=True)
        new_timer.save()
        return Response(new_timer.data, status.HTTP_201_CREATED)
    

class RetrieveUpdateDestroyTimerView(APIView):
    permission_classes = [IsAuthenticated]
    #Show Controller
    #GET /timers/:pk/
    @handle_exceptions
    def get(self, request, pk):
        timer = Timer.objects.filter(user=request.user.id).get(pk=pk)
        serializer = TimerSerializer(timer)
        return Response(serializer.data)
    #keep in mind will want this as a modal in the UI
    

    #Delete Controller
    #DELETE /timers/:pk/
    @handle_exceptions
    def delete(self, request, pk):
        timer = Timer.objects.filter(user=request.user.id).get(pk=pk)  # Get THE timer only for the signed in user
        self.check_object_permissions(request, timer) #Check permissions
        timer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # Update Controller
    # PUT /timers/:pk/
    @handle_exceptions
    def put(self, request, pk):
        timer = Timer.objects.filter(user=request.user.id).get(pk=pk)  # Get THE timer
        self.check_object_permissions(request, timer)

        serializer = TimerSerializer(timer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
