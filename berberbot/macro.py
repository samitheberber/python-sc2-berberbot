import logging
logger = logging.getLogger(__name__)

from sc2.constants import DRONE
from sc2.unit import Unit

from .manager import Manager

class MacroManager(Manager):

    def init(self):
        pass

    async def on_step(self, iteration):
        actions = []
        return actions

    async def on_unit_created(self, unit: Unit):
        logger.info(f"new unit {unit.tag}")
        if unit.type_id == DRONE and unit.is_returning:
            return # Just came out from extractor
        pass

    async def on_unit_destroyed(self, unit_tag):
        logger.warning(f"unit died {unit_tag}")
