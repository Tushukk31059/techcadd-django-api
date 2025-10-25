from django.urls import path
from .views import EnquiryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'enquiry', EnquiryViewSet, basename='enquiry')

urlpatterns = router.urls
