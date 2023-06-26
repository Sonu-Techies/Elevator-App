from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 

from elevator_worklow.models import ElevatorSystem
from elevator_worklow.serializer import ElevatorFactorySerializer


class ElevtoryFactroyViewset(ModelViewSet):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorFactorySerializer

