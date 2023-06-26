from elevator_worklow.models import Elevator, Request

def assign_optmimal_elevator(requested_floor):
    available_elevators = Elevator.objects.filter(is_operational=True, is_in_maintenance=False)
    optimal_elevator = None
    optimal_distance = float('inf')

    for elevator in available_elevators:
        current_floor = elevator.current_floor
        distance = abs(current_floor - requested_floor)

        if elevator.is_moving_up:
            if current_floor <= requested_floor:
                if distance < optimal_distance:
                    optimal_elevator = elevator
                    optimal_distance = distance
        elif elevator.is_moving_down:
            if current_floor >= requested_floor:
                if distance < optimal_distance:
                    optimal_elevator = elevator
                    optimal_distance = distance
        else:  
            if distance < optimal_distance:
                optimal_elevator = elevator
                optimal_distance = distance

    if optimal_elevator:
        Request.objects.create(elevator=elevator, floor=requested_floor)
        return optimal_elevator
    else:
        Request.objects.create(elevator=available_elevators.first(), floor=requested_floor)
        return available_elevators.first()

