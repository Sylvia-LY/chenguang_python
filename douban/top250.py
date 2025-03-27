'''
先找着get的headers (accept, cookie, referer, user agent...)：
1 f12
2 network
3 doc
4 copy as curl (bash)
5 丢进
https://reqbin.com/curl
https://curlconverter.com/
变成python代码
'''

from lxml import etree
import requests
from requests.structures import CaseInsensitiveDict

movies = []

headers = CaseInsensitiveDict()
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cookie"] = """待填"""
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"


def parse_page(url):

    resp = requests.get(url, headers=headers)
    print(resp.status_code)
    root = etree.HTML(resp.text)

    for item in root.xpath("//li/div[@class='item']"):
        # 打印的是lxml的element对象的内存地址。。可读性=0
        # print(i)

        # .// = 从此节点开始往下找
        a_tag = item.xpath(".//div[@class='hd']/a")[0]

        link = a_tag.xpath("@href")[0]
        # 不传参split 按任意长度空白字符(space、newline...)切
        title = ' '.join(''.join(a_tag.itertext()).split())

        movies.append({"title": title, "url": link})

    next_page = root.xpath("//span[@class='next']/a/@href")
    if next_page:
        next_url = "https://movie.douban.com/top250" + next_page[0]
        parse_page(next_url)


parse_page("https://movie.douban.com/top250")

print(f"抓到{len(movies)}部电影")
for m in movies:
    print(f"{m['title']} - {m['url']}")
