from rest_framework import serializers

from api.models import Task, Note


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('deleted', 'is_deleted')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = ('deleted', 'is_deleted')
