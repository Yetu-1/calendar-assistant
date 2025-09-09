import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import AsyncOpenAI
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account key file
SERVICE_ACCOUNT_FILE = "service_account.json"
# Define the scopes
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "davidsalihu20@gmail.com"

# Authenticate and construct service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build("calendar", "v3", credentials=credentials)

events_result = service.events().list(
    calendarId=CALENDAR_ID,
    maxResults=5,
    singleEvents=True,
    orderBy="startTime"
).execute()

events = events_result.get("items", [])
if not events:
    print("No upcoming events.")
else:
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        print(start, event["summary"])

# load_dotenv()
# client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# app = FastAPI()

# class Chat(BaseModel):
#     query: str | None = None


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/assistant")
# async def root(message: Chat):
#     response = await client.responses.create(
#         model="gpt-5",
#         input=message.query
#     )

#     return {"response": response.output_text}