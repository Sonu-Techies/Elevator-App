from rest_framework.routers import DefaultRouter
from elevator_worklow.views import ElevtorFactroyViewset, ElevatorViewSet

router = DefaultRouter()
router.register('elevator-factory',ElevtorFactroyViewset, basename='elevator-factory')
router.register('elevator',ElevatorViewSet, basename='elevator')


urlpatterns=[]
urlpatterns += router.urls