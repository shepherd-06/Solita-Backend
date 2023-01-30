from django.db import models
from uuid import uuid4


# Create your models here.


class Station(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    station_id = models.IntegerField(unique=True)
    name_fi = models.CharField(max_length=50, null=True, default=None)
    name_sw = models.CharField(max_length=50, null=True, default=None)
    name_en = models.CharField(max_length=50, null=True, default=None)
    address_fi = models.CharField(max_length=100,  null=True, default=None)
    address_en = models.CharField(max_length=100,  null=True, default=None)
    city_fi = models.CharField(
        max_length=50,  null=True, blank=True, default=None)
    city_sw = models.CharField(
        max_length=50,  null=True, blank=True, default=None)
    operator = models.CharField(
        max_length=100,  null=True, blank=True, default=None)
    capacity = models.CharField(max_length=10,  null=True, default=None)
    coordinate_x = models.FloatField(null=True, default=None)
    coordinate_y = models.FloatField(null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Station"

    def __str__(self):
        return "{}-{}".format(self.station_id, self.name_fi)
