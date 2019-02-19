import logging
logger = logging.getLogger(__name__)

from .manager import Manager

class MicroManager(Manager):

    async def on_step(self, iteration):
        actions = []
        if len(self.macro.attack_groups) > 0:
            actions += await self.attack_group_actions(iteration)
        return actions

    async def attack_group_actions(self, iteration):
        actions = []
        for group in self.macro.attack_groups:
            actions += group.actions(iteration)
        return actions
