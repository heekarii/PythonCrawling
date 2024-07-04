from bs4 import BeautifulSoup
import requests

with open('C:/Users/hsc06/Downloads/channel_list.txt', 'r') as s:
    urls = s.readlines()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    channel_list = []
    for url in urls:
        response = requests.get(url.strip(), headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            #channel_body = soup.find('head')

            if soup:
                links = soup.find_all('title')
                for link in links:
                    new_chanel = link.get_text().replace(' - YouTube', '')
                    #print(new_chanel)
                    channel_list.append(new_chanel)
                    with open('C:/Users/hsc06/Downloads/qqqq.txt', 'w', encoding='utf-8') as output_file:
                        for text in channel_list:
                            output_file.write(text + '\n')
                    #print(len(channel_list))
            else:
                print(f'{url}No channel found')
