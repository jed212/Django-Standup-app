from rest_framework import serializers
from .models import standup, comments

class standupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = standup
        fields = '__all__'

class commentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comments
        fields = '__all__'