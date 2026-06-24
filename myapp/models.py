from django.db import models

# Create your models here.
class Website(models.Model):

    url = models.CharField(max_length=200)

    status = models.CharField(
        max_length=20,
        blank=True
    )

    response_time = models.FloatField(
        null=True,
        blank=True
    )

    ip_address = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.url