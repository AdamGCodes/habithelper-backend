from rest_framework.serializers import ModelSerializer
from .models import Completed_Habit_Helper


class Completed_Habit_HelperSerializer(ModelSerializer):
    class Meta:
        model = Completed_Habit_Helper
        fields = '__all__'
