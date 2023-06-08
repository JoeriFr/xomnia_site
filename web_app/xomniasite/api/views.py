from django.shortcuts import render
from django.utils.timezone import datetime
from django.db.models import Avg, Min, Max
from django.db.models.functions import TruncHour, TruncDate


from rest_framework import viewsets

from .serializers import (
    MessageSerializer,
    UniqueShipsSerializer,
    AvgSpeedSerializer,
    MinMaxSerializer,
    AllWeatherSerializer,
)
from .models import Message, Data


"""
Setting up the views for API endpoints.

Includes:
- HTTP methods
- Aggregation/grouping/etc
"""

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by("device_id")
    serializer_class = MessageSerializer
    http_method_names = ["get"]


class UniqueShipsViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.order_by().values("device_id").distinct()
    serializer_class = UniqueShipsSerializer
    http_method_names = ["get"]


class AverageSpeedViewSet(viewsets.ModelViewSet):
    queryset = (
        Message.objects.filter(
            datetime_iso__date=datetime(2019, 2, 13).date(), device_id="st-1a2090"
        )
        .annotate(hour=TruncHour("datetime_iso"))
        .values("hour")
        .annotate(avg_speed=Avg("spd_over_grnd"))
        .values("hour", "avg_speed")
    )
    serializer_class = AvgSpeedSerializer
    http_method_names = ["get"]


class MinMaxViewSet(viewsets.ModelViewSet):
    queryset = (
        Data.objects.all()
        .annotate(min_speed=Min("wind_spd"), max_speed=Max("wind_spd"))
        .values("min_speed", "max_speed", "timestamp_utc")
    )
    serializer_class = MinMaxSerializer
    http_method_names = ["get"]


class AllWeatherViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = AllWeatherSerializer
    http_method_names = ["get"]
