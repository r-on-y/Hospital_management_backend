from django.shortcuts import render

from rest_framework import viewsets
from . import models, serializers

class PatientViewset(viewsets.ModelViewSet):
    # Added .objects here
    queryset = models.Patient.objects.all() 
    serializer_class = serializers.PatientSerializer
