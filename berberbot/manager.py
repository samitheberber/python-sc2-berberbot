from sc2.unit import Unit

class Manager:

    def __init__(self, botai):
        self.botai = botai
        self.init()

    def init(self):
        raise NotImplementedError

    async def on_step(self, iteration):
        return []

    async def on_unit_created(self, unit: Unit):
        pass

    async def on_unit_destroyed(self, unit_tag):
        pass

    async def on_building_construction_started(self, unit: Unit):
        pass

    async def on_building_construction_complete(self, unit: Unit):
        pass

    @property
    def macro(self):
        return self.botai.macro

    @property
    def micro(self):
        return self.botai.micro
