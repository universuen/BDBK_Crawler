from Utilities import Spider

if __name__ == '__main__':
    url = "https://baike.baidu.com/item/%E6%AD%A6%E6%B1%89%E5%A4%A7%E5%AD%A6"
    s = Spider(init_url=url, mode="DFS", max_pages=10)
    s.run()