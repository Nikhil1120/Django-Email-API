# Django Email API Project
This project implements a REST API for sending emails using Django and Django REST Framework (DRF). The API allows users to send emails by providing recipient details (email address, subject, and message) through HTTP POST requests.

## Features
- RESTful API: Exposes an API endpoint for sending emails.
- Email Sending: Integrates with Gmail SMTP to send emails securely.
- Email Validation: Validates input data like email addresses and message content.
- Error Handling: Handles various error cases and provides meaningful responses.
- API Testing: Tested using Postman to ensure reliability and robustness.
## Technologies Used
- Django: Web framework for Python used to build the API.
- Django REST Framework (DRF): Simplifies the creation of RESTful APIs in Django.
- Gmail SMTP: Used to send emails through Google's SMTP server.
- Postman: Tool used for API testing.
## Installation
Follow these steps to set up and run the project locally:

### 1. Clone the repository

-- git clone https://github.com/your-username/django-email-api.git
### 2. Navigate into the project directory

-- cd django-email-api
### 3. Set up a virtual environment (optional but recommended)

-- python -m venv venv
Activate the virtual environment:

- For Windows:

-- venv\Scripts\activate
- For macOS/Linux:

-- source venv/bin/activate
### 4. Install dependencies

-- pip install -r requirements.txt
### 5. Set up Gmail SMTP configuration
In settings.py, configure your email settings:


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = 'your-email@gmail.com'  # Your email address

EMAIL_HOST_PASSWORD = 'your-app-password'  # App password generated from Gmail


### 6. Run migrations

python manage.py migrate


### 7. Start the Django development server

python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/send-email/.

API Endpoint
POST /api/send-email/
This endpoint allows you to send emails. It expects a JSON payload with the following fields:

address (required): Recipient's email address.
subject (required): Subject of the email.
message (required): Body of the email.

### 8. Test the API
You can test the email-sending API using Postman:

Set the request type to POST.
Use the URL: http://127.0.0.1:8000/api/send-email/.
In the body, provide the required parameters in JSON format.
