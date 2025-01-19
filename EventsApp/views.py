from django.shortcuts import render
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from django.conf import settings
from .models import EventRegistration

def fetch_and_store_data(request):
  
    credentials = Credentials.from_service_account_file(
        settings.GOOGLE_SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
    )

   
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()

    
    SPREADSHEET_ID = 'eventverse-448213'  
    RANGE = 'Sheet1!A2:E' 

 
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
    values = result.get('values', [])

   
    if values:
        for row in values:
            
            EventRegistration.objects.create(
                name=row[0],
                email=row[1],
                phone_number=row[2],
                interest_level=row[3],
                feedback=row[4],
            )

   
    return render(request, 'registration/success.html', {'count': len(values)})



