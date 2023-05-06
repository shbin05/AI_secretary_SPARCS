from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import os.path

SCOPES = ['https://www.googleapis.com/auth/calendar']

"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

# 기존에 token.json 파일이 있다면 기존 파일을 참조
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

print("구글 계정 인증 완료")

# 서비스 객체 생성
service = build('calendar', 'v3', credentials=creds)

# 캘린더에 추가할 파라미터 생성 및 서비스 객체를 이용한 캘린더 추가
for data in result:
    for val in list:
        calendarData = {
            'summary': "" # 일정 제목
            # 'location': '서울특별시 용산구 한강대로 지하 392', # 일정 장소
            'description': ""  # 일정 설명
            'start': {  # 시작 날짜 (몇시부터~ 일정을 넣고 싶으면 아래 dateTime으로 설정
                'dateTime': '2022-04-22T09:00:00',
                'timeZone': 'Asia/Seoul',
                'date': data[val] if len(data[val].split("~")) == 1 else data[val].split("~")[0] # 하루 종일
            },
            'end': {  # 종료 날짜 (~몇시까지 일정을 넣고 싶으면 아래 dateTime으로 설정)
                'dateTime': '2022-04-25T10:00:00',
                'timeZone': 'Asia/Seoul',
                'date': data[val] if len(data[val].split("~")) == 1 else data[val].split("~")[1] # 하루 종일
            },
            'transparency': 'transparent',
            'reminders': {  # 알림 설정
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 15 * 60},  # 이메일로 알림이 수신됩니다. 24 * 60분 = 하루 전 알림 / 15 * 60 = 하루 전 오전 9시에 알림
                    {'method': 'popup', 'minutes': 15 * 60},  # 핸드폰 팝업으로 뜨게 됩니다.
                ],
            },
        }

        # calendarId : 캘린더 ID. primary이 자기 자신입니다. 다른 캘린더에 작성하고 싶다면 매뉴얼을 참조
        event = service.events().insert(calendarId='primary',
                                        body=calendarData).execute()

        print("Calendar Name : " + event['summary'] + ", Calendar Link : " + event['htmlLink'])

        print("캘린더 추가 완료")