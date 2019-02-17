import sc2

class BerberBot(sc2.BotAI):

    async def on_step(self, iteration):
        if iteration == 0:
            await self.chat_send(f"GLHF")
