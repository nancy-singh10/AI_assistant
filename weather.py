import requests_html


def weather():
    s = requests_html.HTMLSession()
    query = "delhi"
    url = f'https://www.google.com/search?q=weather+{query}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    r = s.get(url, headers=headers)

    temp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
    desc = r.html.find('span#wob_dc', first=True).text
    return temp+" "+unit+" "+desc

