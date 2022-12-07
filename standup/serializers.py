from django.db.models import fields
from rest_framework import serializers
from .models import standup, comments

class standupSerializer(serializers.ModelSerializer):
    class Meta:
        model = standup
        fields = '__all__'

class commentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = '__all__'