## Google Forms Django Database Integration



### Technologies Used

Django: Backend framework.

PostgreSQL: Database.

Google Sheets API: Fetching form responses.

Python Requests: For API key-based integration.


### Requirements

Python 3
Django 
PostgreSQL
Google Cloud project with Sheets API enabled
Access to the Google Sheet containing the form responses

### Setup Instructions

Set Up the Virtual Environment

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate 

### Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

 Configure the Database

Update the DATABASES setting in your settings.py file to connect to your PostgreSQL database.

### Run the migrations:

python manage.py makemigrations

python manage.py migrate

### Set Up Google Sheets API

### Place the JSON file in the project directory and update your settings.py:

SERVICE_ACCOUNT_FILE = 'path/to/your-service-account-file.json'



### Using an API Key

Add the API key in the management command.


### Fetch Google Forms Responses

Run the management command to fetch responses:

python manage.py fetch_responses

