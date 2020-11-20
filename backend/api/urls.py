from rest_framework import routers
from .viewsets import ExampleViewSet

router = routers.DefaultRouter()
router.register('api/example', ExampleViewSet, 'example')

urlpatterns = router.urls