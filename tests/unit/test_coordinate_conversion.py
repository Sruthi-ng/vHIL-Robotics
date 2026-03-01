import pytest
from unittest.mock import MagicMock

def convert_coordinates(x, y, z):
    # Dummy coordinate conversion logic for testing
    return x * 2, y * 2, z * 2

@pytest.mark.navigation
def test_coordinate_conversion_logic():
    # Mocking a coordinate sensor input
    mock_sensor = MagicMock()
    mock_sensor.get_reading.return_value = (10, 20, 30)

    x, y, z = mock_sensor.get_reading()
    result = convert_coordinates(x, y, z)

    assert result == (20, 40, 60)
    mock_sensor.get_reading.assert_called_once()

@pytest.mark.critical
def test_coordinate_conversion_critical_path():
    result = convert_coordinates(0, 0, 0)
    assert result == (0, 0, 0)
