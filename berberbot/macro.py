import logging
logger = logging.getLogger(__name__)

from sc2.constants import DRONE
from sc2.unit import Unit

from .manager import Manager

class MacroManager(Manager):

    def init(self):
        self.our_units = set()
        self.our_buildings = set()

    async def on_step(self, iteration):
        if iteration == 0:
            self.our_units = {unit.tag for unit in self.botai.units.not_structure}
            logger.info(f"our units {len(self.our_units)}")
            self.our_buildings = {unit.tag for unit in self.botai.units.structure}
            logger.info(f"our buildings {len(self.our_buildings)}")
        actions = []
        return actions

    async def on_unit_created(self, unit: Unit):
        logger.info(f"new unit {unit.tag}")
        if unit.type_id == DRONE and unit.is_returning:
            return # Just came out from extractor
        self.our_units.add(unit.tag)

    async def on_unit_destroyed(self, unit_tag):
        if unit_tag in self.our_units:
            self.our_units.remove(unit_tag)
            logger.warning(f"our unit died {unit_tag}")
        elif unit_tag in self.our_buildings:
            self.our_buildings.remove(unit_tag)
            logger.warning(f"our building died {unit_tag}")
        else:
            logger.info(f"something else died {unit_tag}")

    async def on_building_construction_started(self, unit: Unit):
        logger.info(f"new building coming {unit.tag}")
        self.our_buildings.add(unit.tag)

    async def on_building_construction_complete(self, unit: Unit):
        logger.info(f"new building ready {unit.tag}")
