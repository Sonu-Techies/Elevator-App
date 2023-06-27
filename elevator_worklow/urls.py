from rest_framework.routers import DefaultRouter
from elevator_worklow.views import (
    ElevatorSystemViewSet, ElevatorViewSet, ReviewElevatorViewSet, RequestElevatorViewMixin, FloorViewSet
)

router = DefaultRouter()
router.register('elevator-system',ElevatorSystemViewSet, basename='elevator-factory')
router.register('elevator',ElevatorViewSet, basename='elevator')
router.register('review', ReviewElevatorViewSet, basename='review')
router.register('request', RequestElevatorViewMixin, basename='request')
router.register('floor', FloorViewSet, basename='floor')

urlpatterns=[]
urlpatterns += router.urls
