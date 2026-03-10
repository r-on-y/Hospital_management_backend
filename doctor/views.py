from django.shortcuts import render

from rest_framework import viewsets
from . import models, serializers

class DoctorViewset(viewsets.ModelViewSet):
    # Added .objects here
    queryset = models.Doctor.objects.all() 
    serializer_class = serializers.DoctorSerializer


class SpecializationViewset(viewsets.ModelViewSet):
    # Added .objects here
    queryset = models.Specialization.objects.all() 
    serializer_class = serializers.SpecializationSerializer


class AvailableTimeViewset(viewsets.ModelViewSet):
    # Added .objects here
    queryset = models.AvailableTime.objects.all() 
    serializer_class = serializers.AvailableTimeSerializer


class DesignationViewset(viewsets.ModelViewSet):
    # Added .objects here
    queryset = models.Designation.objects.all() 
    serializer_class = serializers.DesignationSerializer



class ReviewViewset(viewsets.ModelViewSet):
    # Added .objects here
    queryset = models.Review.objects.all() 
    serializer_class = serializers.ReviewSerializer
