from __future__ import print_function
import datetime
import calendar
import os.path
from time import strftime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def fetch5Hours():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
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

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='c_eq051skn6egu106p1vqh6ln38o@group.calendar.google.com', timeMin=now,
                                              maxResults=5, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        next_5_events = []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            next_5_events.append(event)
        return next_5_events

    except HttpError as error:
        print('An error occurred: %s' % error)

callAssets = fetch5Hours()

def tillNextHours():
    nextHours = callAssets[0]
    nextHoursStart = nextHours['start'].get('dateTime', nextHours['start'].get('date'))
    datetimeStart = datetime.datetime.strptime(nextHoursStart, '%Y-%m-%dT%H:%M:%S%z')
    formatStart = datetime.datetime.strftime(datetimeStart, '%Y-%m-%d %H:%M:%S')
    reformatStart = datetime.datetime.strptime(formatStart, '%Y-%m-%d %H:%M:%S')
    timeRemaing = reformatStart - datetime.datetime.now()
    return("Time until next hours : " + str(timeRemaing.days) + " days, " + str(timeRemaing.seconds // 3600) + " hours, " + str(timeRemaing.seconds // 60 % 60) + " minutes")

def next5EventsFormatted():
    next5Events = callAssets
    next5EventsFormatted = []
    for event in next5Events:
        next5EventsFormatted.append(event['summary'])
    for i in range(0, 5):
        timeStart = next5Events[i]['start'].get('dateTime', next5Events[i]['start'].get('date'))
        datetimeStart = datetime.datetime.strptime(timeStart, '%Y-%m-%dT%H:%M:%S%z')
        calendarDay = calendar.day_name[datetimeStart.weekday()]
        calendarMonth = calendar.month_name[datetimeStart.month]
        stringFrontAppend = calendarDay + ", " + calendarMonth + ' ' + str(datetimeStart.day)
        startHourAndMinute = str(datetimeStart.hour) + ':' + str(datetimeStart.minute)
        startConvertedToAMPM = datetime.datetime.strftime(datetimeStart, '%I:%M %p')   
        timeEnd = next5Events[i]['end'].get('dateTime', next5Events[i]['end'].get('date'))
        endConvertedToAMPM = datetime.datetime.strftime(datetime.datetime.strptime(timeEnd, '%Y-%m-%dT%H:%M:%S%z'), '%I:%M %p')
        stringBackAppend = startConvertedToAMPM + ' - ' + endConvertedToAMPM
        next5EventsFormatted[i] = "**" + next5EventsFormatted[i] + " : **" + stringFrontAppend + ' ' + stringBackAppend
    return next5EventsFormatted