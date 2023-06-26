from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from .models import ElevatorSystem, Elevator, Floor, ReviewRequestElevator, Request
from .serializers import ElevatorSystemSerializer, ElevatorSerializer, ReviewElevatorRequestedSerializer, RequestSerializer
from .utils import assign_optmimal_elevator


class ElevatorSystemViewSet(viewsets.ModelViewSet):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=False, methods=['post'])
    def initialize_system(self, request):
        num_elevators = request.data.get('num_elevators')
        elevator_system_details = request.data.get('elevator_details', [])
        elevator_system = ElevatorSystem.objects.create(total_elevators=num_elevators)


        for index in range(num_elevators):
            elevated_detail = elevator_system_details[index]
            elevator = Elevator.objects.create(elevator_system=elevator_system, **elevated_detail)

             # Create associated floors for the elevator
            floors = elevated_detail.get('floors', [])
            for floor_number in floors:
                Floor.objects.create(floor_number=floor_number, elevator=elevator)
        return Response({'message': f'Successfully initialized {num_elevators} elevators'})

    @action(detail=True, methods=['get'])
    def fetch_requests(self, request, pk=None):
        """
        API Help to fetch correspondent elevatory request
        """

        elevator = self.get_object()
        requests = elevator.requests.all()
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def next_destination(self, request, pk=None):
        """
        API Give Next feasible Destination
        """

        elevator = self.get_object()
        floors = elevator.floors.all().order_by('floor_number')
        next_floor = None
        for floor in floors:
            if floor.floor_number > elevator.current_floor:
                next_floor = floor.floor_number
                break
        if next_floor is None and floors:
            next_floor = floors[0].floor_number
        return Response({'next_destination': next_floor})

    @action(detail=True, methods=['get'])
    def moving_direction(self, request, pk=None):
        """
        API Gives Moving Direction
        """

        elevator = self.get_object()
        floors = elevator.floors.all().order_by('floor_number')
        if floors:
            if elevator.current_floor < floors[0].floor_number:
                direction = 'up'
            elif elevator.current_floor > floors[0].floor_number:
                direction = 'down'
            else:
                direction = 'stopped'
        else:
            direction = 'stopped'
        return Response({'moving_direction': direction})

    @action(detail=True, methods=['post'])
    def add_request(self, request, pk=None):
        """
        Add Request correspondent floor
        """
        elevator = self.get_object()
        floor_number = request.data.get('floor_number')
        try:
            floor = Floor.objects.get(floor_number=floor_number)
            optimal_elevator = assign_optmimal_elevator(elevator, floor)
            return Response({'message': f'Request added successfully with assigned optimal elevator {optimal_elevator}'})
        except Floor.DoesNotExist:
            return Response({'message': f'Floor {floor_number} does not exist'})

    @action(detail=True, methods=['post'])
    def mark_maintenance(self, request, pk=None):
        elevator = self.get_object()
        elevator.is_operational = False
        elevator.save()
        return Response({'message': 'Elevator marked as not working'})

    @action(detail=True, methods=['post'])
    def open_door(self, request, pk=None):
        elevator = self.get_object()
        if elevator.door_status == 'OPEN':
            return Response({'message': 'Door is already open'}, status=status.HTTP_400_BAD_REQUEST)
        elevator.door_status = 'OPEN'
        elevator.save()
        return Response({'message': 'Door opened'})

    @action(detail=True, methods=['post'])
    def close_door(self, request, pk=None):
        elevator = self.get_object()
        if elevator.door_status == 'CLOSED':
            return Response({'message': 'Door is already closed'}, status=status.HTTP_400_BAD_REQUEST)
        elevator.door_status = 'CLOSED'
        elevator.save()
        return Response({'message': 'Door closed'})

class RequestElevatorViewMixin(
    mixins.UpdateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.CreateModelMixin, 
    mixins.DestroyModelMixin, 
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class ReviewElevatorViewSet(viewsets.ModelViewSet):
    """
    Review Correpondent View Set
    """

    queryset = ReviewRequestElevator.objects.all()
    serializer_class = ReviewElevatorRequestedSerializer
