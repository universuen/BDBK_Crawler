class ModeError(ValueError):
    def __init__(self, mode):
        super()
        self.mode = mode

    def __str__(self):
        return '"mode" should be "BFS" or "DFS", got "%s" instead.'%self.mode
