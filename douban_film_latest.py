import requests
from requests.structures import CaseInsensitiveDict


for page in range(2):
    start=page*20

    url = f"https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start={start}&count=20&selected_categories=%7B%7D&uncollect=false&tags=&ck=_1Nf"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/plain, */*"
    headers["referer"] = "https://movie.douban.com/explore"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        json_data = resp.json()
        for item in json_data['items']:
            # 竟然可以直接用in检查字典中是否包含某个键 无需调用keys
            if 'comment' in item:
                print(item['title'])
                print(item['rating']['value'])
                print(item['uri'])