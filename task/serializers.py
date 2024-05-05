from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    status = serializers.CharField(source='get_status', read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'deadline', 'created_date', 'completed', 'priority','status']