# Website Health Checker

A Django-based web application that monitors website availability and provides basic network diagnostics. Users can enter a website URL and instantly check its status, response time, and IP address.

## Features

- Check website availability (UP/DOWN)
- Measure website response time
- Retrieve website IP address
- Store website monitoring history
- Simple and user-friendly interface
- Built with Django and Python

## Tech Stack

- Python
- Django
- Requests
- SQLite
- HTML
- CSS
- Git & GitHub

## Project Structure

```text
WebsiteMonitor/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   │       └── index.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── README.md
└── db.sqlite3
```

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/WebsiteMonitor.git
cd WebsiteMonitor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## How It Works

1. Enter a website domain (e.g., google.com)
2. Click the **Check** button
3. The application sends an HTTP request to the website
4. It calculates the response time
5. It retrieves the IP address
6. Results are displayed and stored in the database

## Example Output

```text
Website: google.com

Status: UP

Response Time: 124.52 ms

IP Address: 142.250.183.78
```

## Learning Outcomes

- Django Models
- Django Views
- Django Templates
- URL Routing
- Database Operations
- HTTP Requests
- DNS Resolution
- Python Networking
- Git & GitHub Workflow

## Future Enhancements

- SSL Certificate Validation
- Website Uptime Analytics
- Email Alerts
- REST API Integration
- PostgreSQL Support
- Docker Deployment
- Monitoring Dashboard

## Author

**Chandana P**

-
