import sc2

from .macro import MacroManager
from .micro import MicroManager

class BerberBot(sc2.BotAI):

    def on_start(self):
        self.macro = MacroManager(self)
        self.micro = MicroManager(self)

    async def on_step(self, iteration):
        if iteration == 0:
            await self.chat_send(f"GLHF")
