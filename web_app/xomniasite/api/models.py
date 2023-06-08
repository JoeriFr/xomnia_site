from django.db import models

class Message(models.Model):
    device_id = models.CharField(max_length=100)
    datetime = models.BigIntegerField()
    address_ip = models.GenericIPAddressField()
    address_port = models.IntegerField()
    original_message_id = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    lat  = models.FloatField()
    lat_dir = models.CharField(max_length=10)
    lon = models.FloatField()
    lon_dir = models.CharField(max_length=10)
    spd_over_grnd = models.FloatField()
    true_course = models.FloatField()
    datestamp = models.IntegerField()
    mag_variation = models.FloatField()
    mag_var_dir = models.CharField(max_length=10)
    datetime_iso = models.DateTimeField()

    def __str__(self) -> str:
        return self.original_message_id

#######################################################
#
# What I tried with these models here was mapping
# the weather JSON directly to the Django ORM.
# So the end result below is obviously not how I would
# map things in a real situation, I just ended up
# making the least restrictive model possible, but
# still didn't get it to work (because of the foreign
# keys). More explained in ReadMe
#
#######################################################

class Location(models.Model):
	id = models.AutoField(primary_key=True)
	country_code = models.CharField(max_length=100)
	city_name = models.CharField(max_length=100)
	sources = models.CharField(max_length=100)
	timezone = models.CharField(max_length=100)
	station_id = models.CharField(max_length=100)
	lon = models.CharField(max_length=100)
	state_code = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	city_id = models.CharField(max_length=100)
	
class Data(models.Model):
	pod = models.CharField(max_length=100)
	pres = models.CharField(max_length=100)
	azimuth = models.CharField(max_length=100)
	clouds = models.CharField(max_length=100)
	wind_spd = models.FloatField()
	h_angle = models.CharField(max_length=100, null=True, blank=False)
	datetime = models.CharField(max_length=100)
	timestamp_local = models.CharField(max_length=100)
	precip = models.CharField(max_length=100)
	timestamp_utc = models.CharField(max_length=100)
	elev_angle = models.CharField(max_length=100)
	dni = models.CharField(max_length=100)
	vis = models.CharField(max_length=100)
	uv = models.CharField(max_length=100)
	temp = models.CharField(max_length=100)
	dhi = models.CharField(max_length=100)
	ghi = models.CharField(max_length=100)
	dewpt = models.CharField(max_length=100)
	wind_dir = models.CharField(max_length=100)
	solar_rad = models.CharField(max_length=100)
	rh = models.CharField(max_length=100)
	slp = models.CharField(max_length=100)
	snow = models.CharField(max_length=100)
	ts = models.CharField(max_length=100)
	location = models.ForeignKey("Location", on_delete=models.CASCADE, null=True,blank=False)
	
# class Weather(models.Model):
# 	icon = models.CharField(max_length=100)
# 	description = models.CharField(max_length=100)
# 	code = models.CharField(max_length=100)
# 	data = models.OneToOneField(Data,on_delete=models.CASCADE)