from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions,serializers
from .serializers import TodoSerializer
from .models import Todo
from django.core import serializers

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated
# Create your views here.

    def create(self, request):
        todo = Todo.objects.create(title= self.request.data.get('title', ''), description= self.request.data.get('description', ''), user=self.request.user)
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type="application/json")  