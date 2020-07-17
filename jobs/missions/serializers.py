from rest_framework import serializers
from .models import Missions


class MissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = ('id', 'mission', 'is_completed', 'created_at')
