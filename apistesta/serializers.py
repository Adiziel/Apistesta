from rest_framework import serializers
from main.models import Card, SubCard

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCard
        fields = "__all__"