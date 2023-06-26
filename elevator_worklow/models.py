from django.db import models

from core.models import BaseModel
from elevator_worklow.elevator_enum import DirectionStatusEum, DoorStatusEnum 

class ElevatorSystem(BaseModel):
    """
    Model represents the overall elevator system
    """
    total_elevators = models.PositiveIntegerField(default=0)
    maintenance_mode = models.BooleanField(
        default=False, 
        help_text="Indicate whether the elevator is maintaince mode or not"
    )


class Elevator(BaseModel):
    """
    Model represents the detail of indiviual elevator
    """

    elevator_system = models.ForeignKey(ElevatorSystem, on_delete=models.CASCADE, related_name='elevator_factory')
    elevator_name = models.CharField(max_length=100)
    is_operational = models.BooleanField(default=True, help_text="Indicate whether the elevator is operational")
    is_available = models.BooleanField(default=True, help_text="Indicate whether the elevator is available for use")
    current_floor = models.IntegerField(default=0)
    
    status = models.CharField(
        max_length=100,
        choices=DirectionStatusEum.convertable_list(),
        default=DirectionStatusEum.UP.value,
        help_text="Storing the current direction status",
    )
    door_status = models.CharField(
        max_length=100,
        choices=DoorStatusEnum.convertable_list(),
        default=DoorStatusEnum.OPEN.value,
        help_text="Storing the current door status",
    )

    def __str__(self):
        return self.elevator_name


class Floor(BaseModel):
    floor_number = models.IntegerField(unique=True)
    elevator = models.ForeignKey(Elevator, on_delete=models.SET_NULL, null=True, blank=True, related_name='elevator')

    def __str__(self):
        return str(self.floor_number)


class Request(BaseModel):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE, related_name='elevator_request')
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='floor_request')
    request_time = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Request #{self.id}"
