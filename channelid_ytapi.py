import os
from googleapiclient.discovery import build

# API 키 및 API 서비스 이름 설정
api_key = 'AIzaSyBGvD_K-ZTTKAgNucSOFvH7B7Yrbk3eGU4'
api_service_name = 'youtube'
api_version = 'v3'

# YouTube API 클라이언트 생성
youtube = build(api_service_name, api_version, developerKey=api_key)

# set.txt 파일 경로 설정
file_path = 'set.txt'

# set.txt 파일에서 채널명 읽어오기
with open("C:/Users/hsc06/Downloads/set.txt", 'r', encoding='utf-8') as file:
    channel_names = file.read().splitlines()

# 채널 검색 및 채널 ID 가져오기
channel_ids = {}
with open('C:/Users/hsc06/Downloads/channel_ids_4.txt', 'w', encoding='utf-8') as file:
    for channel_name in channel_names:
        search_response = youtube.search().list(
            q=channel_name,
            part='id',
            type='channel'
        ).execute()

        # 첫 번째 검색 결과의 채널 ID 가져오기
        if 'items' in search_response and search_response['items']:
            channel_id = search_response['items'][0]['id']['channelId']
            channel_ids[channel_name] = channel_id
            print(f'{channel_name}의 채널 ID: {channel_id}')
            file.write(f'{channel_name}의 채널 ID: {channel_id}\n')

        else:
            channel_ids[channel_name] = '채널을 찾을 수 없습니다.'

# 결과 출력 또는 다른 작업 수행
# for channel_name, channel_id in channel_ids.items():
