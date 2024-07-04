from bs4 import BeautifulSoup
import requests

with open('C:/Users/hsc06/Downloads/wbe.txt', 'r', encoding='utf-8') as f:
    html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    body_content = soup.find('body')
    channel_list = set()
    cnt = 0

    if body_content:
        titles = soup.find_all('a', attrs={'class': 'name__label'})

        for title in titles:
            new_chanel = title.get_text()
            channel_list.add(new_chanel)
            cnt=cnt +1

    with open('C:/Users/hsc06/Downloads/qqqq.txt', 'r', encoding='utf-8') as s:
        initial_channel = s.readlines()

        for channel in initial_channel:
            channel_list.add(channel.strip())

    with open('C:/Users/hsc06/Downloads/set.txt', 'w', encoding='utf-8') as d:
        for channel in channel_list:
            d.write(f'{channel}\n')

    print(len(initial_channel))
    print(cnt)
    print(len(channel_list))

