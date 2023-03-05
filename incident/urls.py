from rest_framework import routers
from django.urls import include, path
from .views import IncidentViewSet
router = routers.SimpleRouter()
router.register(r'incident', IncidentViewSet,basename='incident')

urlpatterns = router.urls
