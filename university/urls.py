from django.conf.urls import url
from rest_framework import routers
from .views import UniversityViewSet


router = routers.DefaultRouter()
router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls