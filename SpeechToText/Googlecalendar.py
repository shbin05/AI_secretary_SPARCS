from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
event_start = datetime.datetime(2023, 5, 23, 10, 0, 0).isoformat()
print(event_start)
event_end = datetime.datetime(2023, 5, 23, 11, 0, 0).isoformat()
print(event_end)


EVENT = {
  'summary': '',
  'location': '',
  'description': '',
  'start': {
    'dateTime': event_start,
    'timeZone': 'Asia/Seoul',
  },
  'end': {
    'dateTime': event_end,
    'timeZone': 'Asia/Seoul',
  },
}

def change_event(time_obj, text):
    EVENT['start']['dateTime'] = datetime.datetime(int(time_obj.year), int(time_obj.month), int(time_obj.day), int(time_obj.hour), 0, 0).isoformat()
    EVENT['end']['dateTime'] = datetime.datetime(int(time_obj.year), int(time_obj.month), int(time_obj.day), int(time_obj.hour)+1, 0, 0).isoformat()
    EVENT['summary'] = text
    print(EVENT['start']['dateTime'])
    return

def add_calendar(time_obj, text):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    change_event(time_obj, text) 
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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
    try:
        service = build('calendar', 'v3', credentials=creds)
        service.events().insert(calendarId='waniboyy@gmail.com', body=EVENT).execute()
    except HttpError as error:
        print('An error occurred: %s' % error)
