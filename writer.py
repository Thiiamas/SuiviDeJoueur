import core
from oauth2client.service_account import ServiceAccountCredentials

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def write(listofList):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # The ID and range of a sample spreadsheet.
    range = 'Ranked Games!A3:L'

    creds = None
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
        service = build('sheets', 'v4', credentials=creds)

         #Write the values to the spreadsheet
        body = {
            'values': listofList
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=core.document_id, range=range,
            valueInputOption='USER_ENTERED', body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")

    except HttpError as err:
        print(err)


              
                 
    
    