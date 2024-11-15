from rest_framework.serializers import ModelSerializer
from .models import Timer

class TimerSerializer(ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'
