from rest_framework import serializers
from . import models

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        # Changed 'field' to 'fields'
        fields = '__all__'