from __future__ import print_function
import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from dotenv import load_dotenv
import os 
# load .env
load_dotenv()

CLIENT_ID = os.environ.get('GOOGLECALENDAR_client_id_API_KEY')
CLIENT_SECERT = os.environ.get('GOOGLECALENDAR_CLIENTSECRET')

# Use the OAuth credentials to authorize the API client
creds = Credentials.from_authorized_user_info(info={
    "client_id":CLIENT_ID,
    "client_secret":CLIENT_SECERT,
    "refresh_token":"https://oauth2.googleapis.com/token"})

# Build the Calendar API client
calendar_service = build('calendar', 'v3', credentials=creds)

# Set the date and time for the event
event_start = datetime.datetime(2022, 12, 25, 10, 0, 0)
event_end = datetime.datetime(2022, 12, 25, 11, 0, 0)

# Create the event
event = {
    'summary': 'Christmas Day',
    'location': 'Everywhere',
    'description': 'A day to celebrate the birth of Jesus Christ',
    'start': {
        'dateTime': event_start.strftime('%Y-%m-%dT%H:%M:%S'),
        'timeZone': 'UTC',
    },
    'end': {
        'dateTime': event_end.strftime('%Y-%m-%dT%H:%M:%S'),
        'timeZone': 'UTC',
    },
}

# Add the event to the calendar
created_event = calendar_service.events().insert(calendarId='primary', body=event).execute()
print(f'Event created: {created_event.get("htmlLink")}')
