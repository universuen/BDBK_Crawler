from Utilities import Spider

if __name__ == '__main__':
    url = "https://baike.baidu.com/item/%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92%E8%82%BA%E7%82%8E/24282529"
    s = Spider(init_url=url, mode="BFS", max_pages=10)
    s.run()