"""The pc_main component."""
import logging

from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

SENSOR_IDS = [
    "cpu_load",
    "cpu_power",
    "drives_power",
    "fans_power",
    "gpu_load",
    "gpu_power",
    "ram_load",
    "ram_power",
    "total_power",
]

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the pc_main platform."""
    add_entities([PcMainSensor(sensor_id) for sensor_id in SENSOR_IDS])

class PcMainSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, sensor_id):
        """Initialize the sensor."""
        self._sensor_id = sensor_id

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"pc_main.{self._sensor_id}"

    @property
    def unique_id(self):
        """Return a unique ID."""
        return self._sensor_id

    @property
    def state(self):
        """Return the state of the sensor."""
        return 'Your state here'
