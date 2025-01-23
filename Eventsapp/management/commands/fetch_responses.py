import requests
from django.core.management.base import BaseCommand
from django.apps import apps  
from django.conf import settings

API_KEY= settings.API_KEY
SPREADSHEET_ID = settings.SPREADSHEET_ID 
RANGE_NAME = 'Sheet1!A:I'  

class Command(BaseCommand):
    help = 'Fetch Google Forms responses and save them to the database'

    def handle(self, *args, **kwargs):
       
        EventRegistration = apps.get_model('Eventsapp', 'EventRegistration')  

       
        url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{RANGE_NAME}?key={API_KEY}"


        response = requests.get(url)

        if response.status_code != 200:
            self.stderr.write(f"Error fetching data: {response.json().get('error', {}).get('message', 'Unknown error')}")
            return

        data = response.json()
        rows = data.get('values', [])

        if not rows:
            self.stdout.write("No data found in the Google Sheet.")
            return

       
        for row in rows[1:]:  
            try:
                EventRegistration.objects.update_or_create(
             timestamp=row[0],
             defaults={
                 "name": row[1],
                 "email": row[2],
                 "phone_number": row[4],
                 "interest_level": row[5],
                 "feedback":[7]
             }
                )
            except IndexError:
                self.stderr.write(f"Skipping a row due to missing fields: {row}")

        self.stdout.write(self.style.SUCCESS("Successfully fetched and saved responses!"))