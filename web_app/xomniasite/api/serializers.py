from rest_framework import serializers

from .models import Message, Data


"""
Setting up which columns will be used by the API endpoints
"""


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = (
            "id",
            "device_id",
            "datetime",
            "address_ip",
            "address_port",
            "original_message_id",
            "status",
            "lat",
            "lat_dir",
            "lon",
            "lon_dir",
            "spd_over_grnd",
            "true_course",
            "datestamp",
            "mag_variation",
            "mag_var_dir",
            "datetime_iso",
        )


class UniqueShipsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ("device_id",)


class AvgSpeedSerializer(serializers.HyperlinkedModelSerializer):
    avg_speed = serializers.FloatField()
    hour = serializers.CharField()

    class Meta:
        model = Message
        fields = (
            "avg_speed",
            "hour",
        )


class MinMaxSerializer(serializers.HyperlinkedModelSerializer):
    max_speed = serializers.FloatField()
    min_speed = serializers.FloatField()

    class Meta:
        model = Data
        fields = ("min_speed", "max_speed", "timestamp_utc")


class AllWeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = (
            "pod",
            "pres",
            "azimuth",
            "clouds",
            "wind_spd",
            "h_angle",
            "datetime",
            "timestamp_local",
            "precip",
            "timestamp_utc",
            "elev_angle",
            "dni",
            "vis",
            "uv",
            "temp",
            "dhi",
            "ghi",
            "dewpt",
            "wind_dir",
            "solar_rad",
            "rh",
            "slp",
            "snow",
            "ts",
        )
