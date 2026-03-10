from rest_framework import serializers
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    specialization = serializers.StringRelatedField(many=True)
    designation = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)


    class Meta:
        model = models.Doctor
        # Changed 'field' to 'fields'
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Specialization
        # Changed 'field' to 'fields'
        fields = '__all__'


class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        # Changed 'field' to 'fields'
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Designation
        # Changed 'field' to 'fields'
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        # Changed 'field' to 'fields'
        fields = '__all__'