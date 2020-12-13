import queue
from Utilities.Errors import ModeError


class URLManager:
    def __init__(self, mode: str):
        # 根据搜索策略设置数据结构，如果是BFS则使用队列，如果是DFS则使用栈
        if mode in ("BFS", "DFS"):

            self.mode = mode
            if self.mode == "BFS":
                self.container = queue.Queue()
            else:
                self.container = queue.LifoQueue()

            self.used_url = []

        else:
            raise ModeError(mode)

    # 将url存入管理器
    def put(self, url: str):
        if url not in self.used_url:
            self.container.put(url)

    # 从管理器中取出一个url
    def get(self):
        if not self.is_empty():
            url = self.container.get()
            self.used_url.append(url)
            return url

    # 判断管理器是否为空
    def is_empty(self):
        return self.container.empty()
