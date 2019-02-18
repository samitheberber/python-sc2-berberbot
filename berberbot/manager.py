class Manager:

    def __init__(self, botai):
        self.botai = botai
        self.init()

    def init(self):
        raise NotImplementedError

    @property
    def macro(self):
        return self.botai.macro

    @property
    def micro(self):
        return self.botai.micro
