from Utilities import Spider
import time
import os
import shutil


class Estimator:
    def __init__(self, init_url, max_pages):
        assert max_pages > 0
        self.init_url = init_url
        self.max_pages = max_pages
        # 记录不同搜索策略用时
        self.duration = {
            "DFS": 0.0,
            "BFS": 0.0,
        }

    def estimate(self):
        # 评估深度优先搜索
        print("Estimating DFS")
        # 设置文件缓存区
        os.mkdir("./temp")
        spider = Spider(init_url=self.init_url, mode="DFS", path="./temp/", max_pages=self.max_pages)
        start = time.perf_counter()
        spider.run()
        end = time.perf_counter()
        self.duration["DFS"] = end - start
        # 清空缓存
        self._clean()

        # 评估广度优先搜索
        print("Estimating BFS")
        # 设置文件缓存区
        os.mkdir("./temp")
        spider = Spider(init_url=self.init_url, mode="BFS", path="./temp/", max_pages=self.max_pages)
        start = time.perf_counter()
        spider.run()
        end = time.perf_counter()
        self.duration["BFS"] = end - start
        # 清空缓存
        self._clean()

    def _clean(self):
        shutil.rmtree("./temp")

    def show(self):
        # 显示评估结果
        print(f'**********Estimation**********\n'
              f'- Initial URL: {self.init_url}\n'
              f'- Total tested pages: {self.max_pages}\n'
              f'- Time costs:\n'
              f'\t- DFS: {self.duration["DFS"]:.3f} s\n'
              f'\t- BFS: {self.duration["BFS"]:.3f} s\n'
              f'- Speed:\n'
              f'\t- DFS: {self.max_pages/self.duration["DFS"]:.3f} pages per second\n'
              f'\t- BFS: {self.max_pages/self.duration["BFS"]:.3f} pages per second\n')


if __name__ == '__main__':

    url = "https://baike.baidu.com/item/%E6%AD%A6%E6%B1%89%E5%A4%A7%E5%AD%A6"

    # 爬虫功能测试
    s = Spider(init_url=url, mode="DFS", max_pages=3)
    s.run()

    # 爬虫效率评估
    e = Estimator(url, 100)
    e.estimate()
    e.show()
