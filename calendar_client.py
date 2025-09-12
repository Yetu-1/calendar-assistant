import os
from dotenv import load_dotenv
from typing import Optional
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account key file
SERVICE_ACCOUNT_FILE = "service_account.json"
# Define the scopes
SCOPES = ["https://www.googleapis.com/auth/calendar"]
calendar_id = "davidsalihu20@gmail.com"
# Authenticate and construct service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

load_dotenv()

class CalendarClient: 
    def __init__(self):
        self.service = build("calendar", "v3", credentials=credentials) 
    def add_event(self, event_data): 
        event = self.service.events().insert(calendarId=calendar_id, body=event_data).execute()
        # print 'Event created: %s' % (event.get('htmlLink'))

    # def reschedule_event(self, event_id, new_time):


    # def list_events(self, start_time, end_time):
        

    # def check_free_slots(self, start_time, end_time):


# service = build("calendar", "v3", credentials=credentials)

# events_result = service.events().list(
#     calendarId=CALENDAR_ID,
#     maxResults=5,
#     singleEvents=True,
#     orderBy="startTime"
# ).execute()

# events = events_result.get("items", [])
# if not events:
#     print("No upcoming events.")
# else:
#     for event in events:
#         start = event["start"].get("dateTime", event["start"].get("date"))
#         print(start, event["summary"])