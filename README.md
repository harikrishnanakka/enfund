# Django Channels WebSocket Chat Application

This project demonstrates a real-time chat application built with Django Channels, WebSockets, and Redis for message broadcasting. The application allows users to send and receive messages in real-time.

## Requirements

- Python 3.8 or later
- Django 4.0 or later
- Channels
- Redis (for channel layer)

## Setting Up the Project

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your_username/django-channels-chat.git
cd django-channels-chat
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

on windows install:

redis-server

configure djnago settiings:

# settings.py

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],  # Make sure Redis is running
        },
    },
}

ASGI_APPLICATION = 'your_project_name.asgi.application'  # Replace with your project name

migrate the file:

python manage.py migrate

Run the Development server:

python manage.py runserver

Access the Application by seeing the endpoint:

your_project_name/
├── asgi.py            # ASGI application routing
├── consumers.py       # WebSocket consumers
├── settings.py        # Django settings, including CHANNEL_LAYERS configuration
├── urls.py            # URLs configuration
└── wsgi.py            # WSGI application

