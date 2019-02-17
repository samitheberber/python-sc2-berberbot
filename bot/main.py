import json
from pathlib import Path

from berberbot import BerberBot

# Bots are created as classes and they need to have on_step method defined.
# Do not change the name of the class!
class MyBot(BerberBot):
    with open(Path(__file__).parent / "../botinfo.json") as f:
        NAME = json.load(f)["name"]

    async def on_step(self, iteration):
        if iteration == 0:
            await self.chat_send(f"Name: {self.NAME}")
        await super().on_step(iteration)
