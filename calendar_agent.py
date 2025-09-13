from pydantic import BaseModel, Field
from datetime import datetime
from agents import Agent, FunctionTool, function_tool
from calendar_client import CalendarClient
from zoneinfo import ZoneInfo

client = CalendarClient();
time_zone = ZoneInfo("Africa/Lagos")

class DateTime(BaseModel):
    time: datetime = Field(..., description="Event start datetime in RFC3339 format with timezone Africa/Lagos")

class Event(BaseModel):
    summary: str = Field(..., description="Short title for the event")
    location: str | None = Field(None, description="Location of the event")
    description: str | None = Field(None, description="Detailed description of the event")
    start: datetime = Field(..., description="Event start datetime in ISO 8601 format with timezone Africa/Lagos")
    end: datetime = Field(..., description="Event end datetime in ISO 8601 format with timezone Africa/Lagos")

def reformat_event(ai_event):
    # Convert AI event dict to Google Calendar format
    event = {
        "summary": ai_event.summary,
        "location": ai_event.location,
        "description": ai_event.description,
        "start": {
            "dateTime": ai_event.start.astimezone(time_zone).isoformat(),
            "timeZone": "Africa/Lagos"   # you can adjust based on user input
        },
        "end": {
            "dateTime": ai_event.end.astimezone(time_zone).isoformat(),
            "timeZone": "Africa/Lagos"
        },
    }
    return event

@function_tool
def add_event_to_calendar(event: Event) -> str:
    """Add a new event to the calendar.

    Args:
        event: The event object containing title, start/end time, location, and description.
    """
    # Convert to dict for serialization
    event_data = reformat_event(event)
    print(event_data)
    client.add_event(event_data)
    # In real life, we'd insert this into Google Calendar or a database
    return (
        f"✅ Event '{event.summary}' added\n"
        f"- Start: {event.start.dt} ({event.start.timezone})\n"
        f"- End: {event.end.dt} ({event.end.timezone})\n"
        f"- Location: {event.location or 'N/A'}\n"
        f"- Description: {event.description or 'N/A'}"
    )

@function_tool
def get_calendar_events(time_min: DateTime, time_max: DateTime) -> str:
    """Get events within a time range from the calender.

    Args:
        time_min: the lower bound for the event start time (inclusive).
        time_max: the upper bound for the event start time (exclusive).
        Both must be in RFC3339 format (YYYY-MM-DDTHH:MM:SS+00:00).
    """
    start_time = time_min.time.astimezone(time_zone).isoformat()
    end_time = time_max.time.astimezone(time_zone).isoformat()
    client.list_events(start_time, end_time)
    # In real life, we'd insert this into Google Calendar or a database
    return (
        f"✅ Event '{event.summary}' added\n"
        f"- Start: {event.start.dt} ({event.start.timezone})\n"
        f"- End: {event.end.dt} ({event.end.timezone})\n"
        f"- Location: {event.location or 'N/A'}\n"
        f"- Description: {event.description or 'N/A'}"
    )


calendar_agent = Agent(
    name="calendar_agent",
    instructions=(
        "You are a calendar management agent. You use the provided tools to manage the user's calendar. "
        "If the user wants to create, add to calendar, reschedule, list events, or check availability, "
        "you must call the appropriate tool. "
        "You never modify the calendar directly, you always use the tools."
    ),
    tools=[add_event_to_calendar, get_calendar_events],
)
