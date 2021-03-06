from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("id","code","host","guess_time","created_at")

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["guess_time"]
