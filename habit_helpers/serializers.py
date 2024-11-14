from rest_framework.serializers import ModelSerializer
from .models import Habit_Helper
from users.serializers import UserSerializer


class Habit_HelperSerializer(ModelSerializer):
    class Meta:
        model = Habit_Helper
        fields = '__all__'
