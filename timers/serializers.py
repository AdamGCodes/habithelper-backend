from rest_framework.serializers import ModelSerializer
from .models import Timer
from users.serializers import UserSerializer

class TimerSerializer(ModelSerializer):
    class Meta:
        model = Timer
        fields = ('name', 'reason', 'started', 'exceptions')
