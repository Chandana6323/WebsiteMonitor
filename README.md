# 🌐 Website Health Checker

A Django-based Website Health Checker that monitors website availability, performs DNS resolution, measures HTTP response times, and displays basic network diagnostics.

## 🚀 Features

- Website Availability Check (UP/DOWN)
- HTTP Response Monitoring
- Response Time Measurement
- DNS Resolution
- IP Address Retrieval
- Monitoring History Storage
- Simple Web Interface

## 🛠️ Tech Stack

- Python
- Django
- Requests
- Socket Programming
- SQLite
- HTML
- Git
- GitHub

## 🌐 Networking Concepts Used

### DNS Resolution

Converts domain names into IP addresses using Python's socket module.

```python
import socket

ip_address = socket.gethostbyname("google.com")
print(ip_address)
```

### HTTP Monitoring

Checks website availability using HTTP requests.

```python
import requests

response = requests.get("https://google.com")
print(response.status_code)
```

### Response Time Measurement

Measures how quickly a website responds.

```python
import time
import requests

start = time.time()
requests.get("https://google.com")
end = time.time()

response_time = (end - start) * 1000
```

## 📊 Example Output

```text
Website: google.com

Status: UP

Response Time: 128.54 ms

IP Address: 142.250.183.78
```

## 🎯 Skills Demonstrated

- Python Programming
- Django Development
- Backend Development
- Database Operations
- HTTP Protocol
- DNS Resolution
- Socket Programming
- Network Diagnostics
- Website Monitoring
- Git & GitHub

## 📚 Learning Outcomes

- Django Models, Views, and Templates
- HTTP Request Handling
- DNS Lookup Mechanisms
- Network Programming in Python
- Website Performance Monitoring
- Backend Application Development
- Database Management

## 🔮 Future Enhancements

- SSL Certificate Validation
- Website Uptime Analytics
- Email Alerts
- REST API Integration
- PostgreSQL Database
- Docker Deployment
- Multi-Website Monitoring

## 👩‍💻 Author

**Chandana P**

