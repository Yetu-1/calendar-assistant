import os
from dotenv import load_dotenv
from typing import Optional
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()
calendar_id = AsyncOpenAI(api_key=os.getenv("CALENDAR_ID"))

class CalendarClient: 
    def __init__(self, credentials):
        self.service = build("calendar", "v3", credentials=credentials) 

    def add_event(self, event_data): 
        event = self.service.events().insert(calendarId=calendar_id, body=event_data).execute()
        print 'Event created: %s' % (event.get('htmlLink'))

    def reschedule_event(self, event_id, new_time):

    def list_events(self, start_time, end_time):

    def check_free_slots(self, start_time, end_time):