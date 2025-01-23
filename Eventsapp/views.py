# import os
# from googleapiclient.discovery import build
# from google.oauth2 import service_account
# from .models import EventRegistration


# SERVICE_ACCOUNT_FILE = 'service-account-key.json'


# SPREADSHEET_ID = '1WBEHFfkLK2UX7uzowdbL8BZkqySWb6IbKZ1fnRhmP0w'
# RANGE_NAME = 'Sheet1!A:I' 

# def fetch_and_save_responses():

#     credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE,
#         scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
#     )
#     service = build('sheets', 'v4', credentials=credentials)
#     sheet = service.spreadsheets()

  
#     result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
#     rows = result.get('values', [])

   
#     for row in rows[1:]: 
#         EventRegistration.objects.update_or_create(
#             timestamp=row[0],
#             defaults={
#                 "name": row[1],
#                 "email": row[2],
#                 "phone_number": row[4],
#                 "interest_level": row[5],
#                 "feedback":[7]
#             }
#         )