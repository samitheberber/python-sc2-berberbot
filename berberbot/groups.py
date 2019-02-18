class AttackGroup:
    def __init__(self, botai, own, targets, iter):
        self.botai = botai
        self.own = own
        self.targets = targets
        self.iteration = iter

    @property
    def done(self):
        return len(self.own) == 0 or len(self.targets) == 0

    def actions(self, iter):
        actions = []
        target_units = self.botai.known_enemy_units.tags_in(self.targets)
        if target_units.exists:
            target = target_units.first
            for unit in self.botai.units.tags_in(self.own):
                actions.append(unit.attack(target))
        else:
            self.targets = set() #lost targets
        return actions

    def clear_tag(self, tag):
        if tag in self.own:
            self.own.remove(tag)
        elif tag in self.targets:
            self.targets.remove(tag)
