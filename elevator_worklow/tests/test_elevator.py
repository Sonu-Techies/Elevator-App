from rest_framework import status
import pytest
from model_bakery import baker
from ..models import Elevator, ElevatorSystem

@pytest.fixture
def create_elevator(api_client):
    def de_create_elevator(collection):
        return api_client.post('/api/elevator/', collection)
    return de_create_elevator


@pytest.mark.django_db
class TestCreateElevator:

    def test_if_data_is_valid_returns_201(self):
        elevator_system = baker.make(ElevatorSystem)
        response = create_elevator(
            {'elevator_system': elevator_system, 'elevator_name': "Citizen Elevator"}
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
