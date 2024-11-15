from rest_framework.serializers import ModelSerializer
from .models import Timer
from users.serializers import UserSerializer

class TimerSerializer(ModelSerializer):
    class Meta:
        model = Timer
        fields = ('id', 'name', 'reason', 'started', )
        read_only_fields = ('user', 'created_at', 'updated_at') 
