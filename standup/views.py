from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import commentsSerializer, standupSerializer
from .models import standup, comments

class standupViewset(viewsets.ModelViewSet):
    queryset= standup.objects.all()
    serializer_class = standupSerializer
    permission_classes = [permissions.IsAuthenticated]


class commentsViewset(viewsets.ModelViewSet):
    queryset = comments.objects.all()
    serializer_class = commentsSerializer
    permission_classes = [permissions.IsAuthenticated]

