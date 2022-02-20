from django.db import models


class Data(models.Model):
    site_name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField()
    datastream = models.TextField()
