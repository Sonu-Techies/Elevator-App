from rest_framework.serializers import ModelSerializer, Serializer
from elevator_worklow.models import ElevatorSystem

class ElevatorFactorySerializer(ModelSerializer):
    """
    Elevator Serilaizer
    """

    class Meta:
        models = ElevatorSystem
        fields = ['total_elevators', 'maintenance_mode']

