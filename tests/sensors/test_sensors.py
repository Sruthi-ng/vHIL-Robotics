import pytest
from unittest.mock import MagicMock

class ForceSensor:
    def read_force(self):
        pass

class ProximitySensor:
    def read_distance(self):
        pass

class OpticalSensor:
    def check_visibility(self):
        pass

@pytest.mark.sensor
def test_force_sensor_simulation():
    sensor = ForceSensor()
    sensor.read_force = MagicMock(return_value=15.5)
    
    assert sensor.read_force() == 15.5
    sensor.read_force.assert_called_once()

@pytest.mark.sensor
def test_proximity_sensor_simulation():
    sensor = ProximitySensor()
    sensor.read_distance = MagicMock(return_value=5.0)
    
    assert sensor.read_distance() == 5.0
    sensor.read_distance.assert_called_once()

@pytest.mark.sensor
@pytest.mark.critical
def test_optical_sensor_simulation():
    sensor = OpticalSensor()
    sensor.check_visibility = MagicMock(return_value=True)
    
    assert sensor.check_visibility() is True
    sensor.check_visibility.assert_called_once()
