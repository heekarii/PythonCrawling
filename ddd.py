from bs4 import BeautifulSoup
import requests


def start_with_yt(tag):
    return tag.name == 'a' and tag.get('href', '').startswith('https://www.youtube.com/channel')


with open('C:/Users/hsc06/Downloads/set.txt', 'r', encoding='utf-8') as f:
    channel_names = [channel_name.strip() for channel_name in f.readlines()]
    all_links = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    if channel_names:
        for channel in channel_names:
            url = "https://www.google.com/search?q=" + channel
            result = requests.get(url, headers=headers)
            soup = BeautifulSoup(result.text, "html.parser")

            channel_links = soup.find(start_with_yt)

            if channel_links:
                all_links.append(channel_links['href'])
                print(channel_links['href'])
            else:
                print('No channel found')
    else:
        print('No channel found')

    if all_links:
        with open('C:/Users/hsc06/Downloads/aaaa.txt', 'w') as output_file:
            for text in all_links:
                output_file.write(text + '\n')
    else:
        print('No links found')
