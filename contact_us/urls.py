from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

# Fixed spelling
router = DefaultRouter()
router.register('contact_us', views.ContactUsViewset)

urlpatterns = [
    # Fixed the period at the end
    path('', include(router.urls)),
]