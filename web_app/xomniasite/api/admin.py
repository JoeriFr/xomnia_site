from django.contrib import admin
from .models import Message, Location, Data
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field


# Creating API resources
class MessageResource(resources.ModelResource):
   class Meta:
      model = Message
class MessageAdmin(ImportExportModelAdmin):
   resource_class = MessageResource

class LocationResource(resources.ModelResource):
   class Meta:
      model = Location
class LocationAdmin(ImportExportModelAdmin):
   resource_class = LocationResource

class DataResource(resources.ModelResource):
   location = Field(
        widget=ForeignKeyWidget(model=Location, use_natural_foreign_keys=True))
   class Meta:
      model = Data
class DataAdmin(ImportExportModelAdmin):
   resource_class = DataResource


# class WeatherResource(resources.ModelResource):
#    class Meta:
#       model = Weather
# class WeatherAdmin(ImportExportModelAdmin):
#    resource_class = WeatherResource

# admin.site.register(Weather)

# Regestring models + allowing uploading files through admin portal
admin.site.register(Data, DataAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Location, LocationAdmin)