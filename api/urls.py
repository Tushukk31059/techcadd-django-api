from rest_framework import routers
from .views import EnquiryViewSet

router = routers.DefaultRouter()
router.register('enquiry', EnquiryViewSet)

urlpatterns = router.urls
