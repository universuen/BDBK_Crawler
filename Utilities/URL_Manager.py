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

            self.used_url = []

        else:
            raise ModeError(mode)


    def put(self, url:str):
        if url not in self.used_url:
            self.container.put(url)


    def get(self):
        if not self.is_empty():
            url = self.container.get()
            self.used_url.append(url)
            return url


    def is_empty(self):
        return self.container.empty()
