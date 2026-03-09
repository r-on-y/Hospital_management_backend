from django.shortcuts import render

from rest_framework import viewsets
from . import models, serializers

class ServiceViewset(viewsets.ModelViewSet):
    # Added .objects here
    queryset = models.Service.objects.all() 
    serializer_class = serializers.ServiceSerializer
