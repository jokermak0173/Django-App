from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = Task
        fields = ['user', 'id', 'title', 'description', 'is_completed', 'priority']
    
    def get_user(self, Task):
        return {
            'user_id': Task.user.id,
            'user_full_name': Task.user.get_full_name(),
        }
    