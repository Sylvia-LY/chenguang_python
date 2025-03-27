from bs4 import BeautifulSoup
import requests
from requests.structures import CaseInsensitiveDict
import csv

movies = []

headers = CaseInsensitiveDict()
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cookie"] = """待填"""
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"


def parse_page(url, watched_flag):
    print(f"正在抓：{url}")

    resp = requests.get(url, headers=headers)    
    soup = BeautifulSoup(resp.text, 'lxml')

    for a in soup.select('li.title a'):

        link = a['href']
        title = a.get_text(strip=True)

        movies.append({"watched": watched_flag, "title": title, "url": link})
    
    next_page = soup.select_one('span.next a')
    if next_page:
        next_url = "https://movie.douban.com" + next_page['href']
        parse_page(next_url, watched_flag)


parse_page("https://movie.douban.com/mine?status=collect", True)
parse_page("https://movie.douban.com/mine?status=wish", False)

with open("watchlist.csv", "w", encoding="utf-8-sig", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["watched", "title", "url"])
    writer.writeheader()
    writer.writerows(movies)


print(f"已保存{len(movies)}部电影到watchlist.csv")
