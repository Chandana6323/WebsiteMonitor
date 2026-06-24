import requests
import socket
import time

from django.shortcuts import render
from .models import Website


def home(request):

    if request.method == "POST":

        website = request.POST["url"]

        start = time.time()

        try:

            requests.get(
                f"https://{website}",
                timeout=5
            )

            end = time.time()

            response_time = round(
                (end - start) * 1000,
                2
            )

            status = "UP"

            ip = socket.gethostbyname(
                website
            )

        except:

            response_time = 0

            status = "DOWN"

            ip = "Not Found"

        Website.objects.create(
            url=website,
            status=status,
            response_time=response_time,
            ip_address=ip
        )

    websites = Website.objects.all()

    return render(
        request,
        'myapp/index.html',
        {
            'websites': websites
        }
    )