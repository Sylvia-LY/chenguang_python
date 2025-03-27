from bs4 import BeautifulSoup
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
    
    soup = BeautifulSoup(resp.text, 'lxml')

    for item in soup.select('div.item'):

        a_tag = item.select_one('div.hd a')

        link = a_tag['href']
        title = ' '.join(a_tag.stripped_strings)

        movies.append({"title": title, "url": link})

    next_page = soup.select_one('span.next a')
    if next_page:
        next_url = "https://movie.douban.com/top250" + next_page['href']
        parse_page(next_url)


parse_page("https://movie.douban.com/top250")

print(f"抓到{len(movies)}部电影")
for m in movies:
    print(f"{m['title']} - {m['url']}")
