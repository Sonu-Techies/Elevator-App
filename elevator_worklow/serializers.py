from rest_framework import serializers
from .models import ElevatorSystem, Elevator, Floor, Request, ReviewRequestElevator

class ElevatorSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorSystem
        fields = '__all__'

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = [
            'elevator_system',
            'elevator_name',
            'is_operational',
            'is_available',
            'current_floor',
            'status',
            'door_status'
        ]

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
            'elevator',
            'floor',
            'is_completed'
        ]

class ReviewElevatorRequestedSerializer(serializers.ModelSerializer):
     class Meta:
        model = ReviewRequestElevator
        fields = [
            'elevator',
            'request',
            'rating',
            'comment'
        ]
