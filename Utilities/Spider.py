import requests
from bs4 import BeautifulSoup
from Utilities import URLManager
from Utilities.UA_LIST import USER_AGENT_LIST
import random
import re


def get_html(url):
    ua = random.choice(USER_AGENT_LIST)
    headers = {'user-agent': ua}
    html = requests.get(url, headers=headers).content
    return html


class Spider:
    def __init__(self, init_url: str, mode: str, path: str = "./", max_pages: int = 100):
        # 设置爬行模式
        self.url_manager = URLManager(mode)
        # 将第一个url放入url管理器
        self.url_manager.put(init_url)
        # 设置存储路径
        self.path = path
        # 设置计数器
        self.count = max_pages

    def run(self):
        # 当url管理器非空时循环
        while not self.url_manager.is_empty():
            # 从url管理器取出一个url进行爬取
            url = self.url_manager.get()
            # 获取网页源码
            html = get_html(url)
            # 初始化一个解析器
            soup = BeautifulSoup(html, features="html.parser")
            # 获取网页标题
            title = soup.find("title").text
            # 获取网页内容
            raw_content = soup.find_all(class_="para")

            # 将爬取到的网页内容存储至本地
            with open(self.path + title + ".txt", "w", encoding='utf-8') as f:
                print(title)
                for i in raw_content:
                    f.write(i.text)

            # 从网页中解析出新的url
            raw_urls = soup.find_all('a', target="_blank", href=re.compile(r"/item/(.*?)"),
                                     attrs={"data-lemmaid": re.compile(r"(.*?)")})

            # 将新的url加入url管理器
            for i in raw_urls:
                new_url = "https://baike.baidu.com" + i.attrs['href']
                # print(new_url)
                self.url_manager.put(new_url)

            # 当计数器为0时退出
            self.count -= 1
            if self.count == 0:
                break
