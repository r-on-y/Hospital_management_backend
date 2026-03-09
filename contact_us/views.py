from rest_framework import viewsets
from . import models, serializers

class ContactUsViewset(viewsets.ModelViewSet):
    # Added .objects here
    queryset = models.ContactUs.objects.all() 
    serializer_class = serializers.ContactUsSerializer