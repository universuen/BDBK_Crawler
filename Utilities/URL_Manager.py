import queue
from Utilities.Errors import ModeError


class URL_Manager:
    def __init__(self, mode:str):
        if mode in ("BFS", "DFS"):

            self.mode = mode
            if self.mode == "BFS":
                self.container = queue.Queue()
            else:
                self.container = queue.LifoQueue()

        else:
            raise ModeError(mode)


    def put(self, url:str):
        self.container.put(url)


    def get(self):
        if not self.is_empty():
            return self.container.get()


    def is_empty(self):
        return self.container.empty()
