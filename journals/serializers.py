from rest_framework.serializers import ModelSerializer
from .models import Journal

class JournalSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'