import requests
from requests.structures import CaseInsensitiveDict
from lxml import etree

pages = 3
# 豆瓣图书标签：编程
url = "https://book.douban.com/tag/%E7%BC%96%E7%A8%8B"

headers = CaseInsensitiveDict()
# 设置请求头 这3条加上基本能通过 1 我用的哪种浏览器
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
# 2 我打哪个页面来
headers["referer"] = "https://book.douban.com/"
# 3 我想要的是什么
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"

while 1:
    resp = requests.get(url, headers=headers)

    # 如果get请求成功
    if (resp.status_code==200):
        tree = etree.HTML(resp.content)

        # 遍历这一页的图书条目
        for book in tree.xpath("//li[@class='subject-item']"):

            for title in book.xpath('.//h2/a'):
                print(''.join(text.strip() for text in title.itertext() if text.strip()))
            
            price = book.xpath(".//span[@class='buy-info']/a/text()")
            if price:
                # 清理价格数据
                # 现在功能上没问题。。如果价格一行还有其她'.'就麻烦了 实在不行上正则吧
                price = ''.join(c for c in price[0] if c.isdigit() or c=='.').strip()
            else:
                price = -1
            print(float(price))

        # extract后页链接
        next_page = tree.xpath("//span[@class='next']/a/@href")
        if next_page:
            url = "https://book.douban.com"+next_page[0]
        else:
            break

    pages -= 1
    if pages==0:
        break