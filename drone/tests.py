from django.test import TestCase

from .models import Drone, Medication, Shipping

# Create your tests here.


class DroneModelTest(TestCase):

    def setUp(self):
        data = {
            'serial_number': '135486568754687',
            'weigth_limit': 250.0,
            'battery_capacity': 50,
        }
        self.drone = Drone.objects.create(**data)

    def test_default_fields(self):
        """Test case to verify default fields"""
        self.assertEquals(self.drone.model, Drone.DroneModel.LIGHTWEIGHT)
        self.assertEquals(self.drone.state, Drone.Status.IDLE)
