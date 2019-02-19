import sc2
from sc2.unit import Unit

from .macro import MacroManager
from .micro import MicroManager
from .bo import BuildOrder

class BerberBot(sc2.BotAI):

    def on_start(self):
        self.macro = MacroManager(self)
        self.micro = MicroManager(self)
        self.bo = BuildOrder(self)

    def on_end(self, game_result):
        pass

    def _prepare_first_step(self):
        super()._prepare_first_step()
        self.expansion_locations # cache expansion locations

    async def on_step(self, iteration):
        actions = []
        actions += await self.macro.on_step(iteration)
        actions += await self.micro.on_step(iteration)
        await self.do_actions(actions)

        if iteration == 0:
            await self.chat_send(f"GLHF")
            await self.chat_send(f"All {len(self.expansion_locations)} expansions belong to me!")

    async def on_unit_created(self, unit: Unit):
        await self.macro.on_unit_created(unit)
        await self.micro.on_unit_created(unit)

    async def on_unit_destroyed(self, unit_tag):
        await self.macro.on_unit_destroyed(unit_tag)
        await self.micro.on_unit_destroyed(unit_tag)

    async def on_building_construction_started(self, unit: Unit):
        await self.macro.on_building_construction_started(unit)
        await self.micro.on_building_construction_started(unit)

    async def on_building_construction_complete(self, unit: Unit):
        await self.macro.on_building_construction_complete(unit)
        await self.micro.on_building_construction_complete(unit)
