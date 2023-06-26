from rest_framework.routers import DefaultRouter
from elevator_worklow.views import ElevatorSystemViewSet, ElevatorViewSet

router = DefaultRouter()
router.register('elevator-system',ElevatorSystemViewSet, basename='elevator-factory')
router.register('elevator',ElevatorViewSet, basename='elevator')


urlpatterns=[]
urlpatterns += router.urls