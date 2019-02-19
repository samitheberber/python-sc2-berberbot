import enum

from sc2.constants import DRONE, LARVA, OVERLORD
from sc2.cache import property_cache_once_per_frame

from .manager import Manager

class BOType(enum.Enum):
    FROM_LARVA = 0
    FROM_DRONE = 1
    FROM_TOWNHALL = 2

class BuildOrder(Manager):

    @property_cache_once_per_frame
    def next(self):
        return BOType.FROM_LARVA, DRONE
