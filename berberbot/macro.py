import logging
logger = logging.getLogger(__name__)

from sc2.constants import DRONE
from sc2.unit import Unit

from .manager import Manager
from .groups import AttackGroup

class MacroManager(Manager):

    def init(self):
        self.our_units = set()
        self.our_buildings = set()
        self.attack_groups = []

    async def on_step(self, iteration):
        if iteration == 0:
            self.our_units = {unit.tag for unit in self.botai.units.not_structure}
            logger.info(f"our units {len(self.our_units)}")
            self.our_buildings = {unit.tag for unit in self.botai.units.structure}
            logger.info(f"our buildings {len(self.our_buildings)}")

        await self.update_attack_groups(iteration)
        actions = []
        return actions

    async def on_unit_created(self, unit: Unit):
        logger.info(f"new unit {unit.tag}")
        if unit.type_id == DRONE and unit.is_returning:
            return # Just came out from extractor
        self.our_units.add(unit.tag)

    async def on_unit_destroyed(self, unit_tag):
        for group in self.attack_groups:
            group.clear_tag(unit_tag)
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

    async def update_attack_groups(self, iteration):
        for group in self.attack_groups:
            if group.done:
                self.attack_groups.remove(group)
                logger.warning(f"Group done")
        if self.botai.known_enemy_units.exists:
            enemies = [u.tag for u in self.botai.known_enemy_units]
            if len(self.attack_groups) == 0:
                my_units = [u.tag for u in self.botai.units(DRONE)]
                if len(my_units) > 0:
                    logger.warning(f"Naive group to go!")
                    fresh_group = AttackGroup(self.botai, my_units, enemies, iteration)
                    self.attack_groups.append(fresh_group)
